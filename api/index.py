import os
import sys
import logging
import traceback
from fastapi import FastAPI, Request, Response
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# VERSION TAG (Diagnostic)
VERSION = "1.0.5"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Error storage
LAST_ERRORS = []

# Add root directory to sys.path to import bot.py and config.py
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Import bot and dp from bot.py
try:
    from bot import dp, bot
    from config import BOT_TOKEN
except Exception as e:
    logger.error(f"Import error: {e}")
    LAST_ERRORS.append(f"Import Error: {traceback.format_exc()}")
    dp = None
    bot = None

app = FastAPI()

async def process_update(request: Request):
    if dp is None or bot is None:
        return {"error": "Bot/DP not initialized", "version": VERSION}, 500
    
    try:
        data = await request.json()
        logger.info(f"Update received [{VERSION}]: {data}")
        
        # Hydrate with bot context (critical for aiogram 3.x Command filters)
        update = types.Update.model_validate(data, context={"bot": bot})
        
        # Feed the update
        await dp.feed_update(bot, update)
        return {"ok": True, "version": VERSION}
    except Exception as e:
        err_msg = traceback.format_exc()
        logger.error(f"Execution Error: {err_msg}")
        LAST_ERRORS.append(f"Execution Error: {err_msg}")
        return {"ok": False, "error": str(e), "version": VERSION}

@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(path_name: str, request: Request):
    """
    Catch-all route with strict version reporting.
    """
    if request.method == "POST":
        return await process_update(request)
    
    # Handle GET Diagnostic
    if path_name == "api/check":
        try:
            me = await bot.get_me() if bot else "Not Init"
            return {
                "status": "ok",
                "version": VERSION,
                "bot": me.username if not isinstance(me, str) else me,
                "handlers": len(dp.message.handlers) if dp else 0
            }
        except Exception as e:
            return {"status": "error", "error": str(e), "version": VERSION}
            
    if path_name == "api/logs":
        return {"errors": LAST_ERRORS[-10:], "version": VERSION}

    return {
        "status": "bot is running",
        "version": VERSION,
        "path": path_name,
        "bot_initialized": bot is not None
    }

# Explicit root handlers
@app.get("/")
async def root_get():
    return {"status": "bot is running", "at": "root", "version": VERSION}

@app.post("/")
async def root_post(request: Request):
    return await process_update(request)

import os
import sys
import logging
import traceback
from fastapi import FastAPI, Request, Response
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

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

# --- Emergency Handler ---
async def emergency_start(message: types.Message):
    """
    This handler is registered directly in the entry point.
    If this works, it means the bot is alive but bot.py handlers are failing.
    """
    try:
        await message.answer("🚨 EMERGENCY START ACTIVE 🚨\n\nIf you see this, the bot is connected. Now processing your request...")
    except Exception as e:
        logger.error(f"Emergency handler error: {e}")
        LAST_ERRORS.append(f"Answer Error: {str(e)}")

# Add the emergency handler to the dispatcher
if dp:
    # Use a high priority handler to bypass others
    @dp.message(Command("emergency"))
    async def msg_emergency(message: types.Message):
        await message.answer("Diagnostic: Bot is receiving messages.")

async def process_update(request: Request):
    if dp is None or bot is None:
        return {"error": "Bot/DP not initialized"}, 500
    
    try:
        data = await request.json()
        logger.info(f"Update: {data}")
        
        # Hydrate
        update = types.Update(**data)
        
        # Feed
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        err_msg = traceback.format_exc()
        logger.error(f"Execution Error: {err_msg}")
        LAST_ERRORS.append(f"Execution Error: {err_msg}")
        return {"ok": False, "error": str(e)}

@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(path_name: str, request: Request):
    if request.method == "POST":
        return await process_update(request)
    
    # Handle GET
    if path_name == "api/check":
        try:
            me = await bot.get_me() if bot else "Not Init"
            return {
                "status": "ok",
                "bot": me.username if not isinstance(me, str) else me,
                "handlers": len(dp.message.handlers) if dp else 0
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
            
    if path_name == "api/logs":
        return {"errors": LAST_ERRORS[-10:]} # Return last 10 errors

    return {"status": "bot is running", "path": path_name}

@app.get("/")
async def root_get():
    return {"status": "bot is running", "at": "root"}

@app.post("/")
async def root_post(request: Request):
    return await process_update(request)

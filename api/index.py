import os
import sys
import logging
from fastapi import FastAPI, Request, Response
from aiogram import Bot, Dispatcher, types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    dp = None
    bot = None

app = FastAPI()

@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(path_name: str, request: Request):
    if request.method == "POST":
        try:
            data = await request.json()
            logger.info(f"Update: {data}")
            
            # Use the most basic update creation (known to work in Turn 31)
            update = types.Update(**data)
            
            # Feed the update into the dispatcher
            await dp.feed_update(bot, update)
            return {"ok": True}
        except Exception as e:
            logger.error(f"Error: {e}", exc_info=True)
            return {"ok": False, "error": str(e)}
    
    # Handle GET
    if path_name == "api/check":
        try:
            me = await bot.get_me()
            # Check for handlers
            handler_count = len(dp.message.handlers) + len(dp.callback_query.handlers)
            return {
                "status": "ok",
                "bot": me.username,
                "token_prefix": BOT_TOKEN[:10] if BOT_TOKEN else "missing",
                "handlers_registered": handler_count,
                "venv": sys.version
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}

    return {"status": "bot is running", "at": path_name}

@app.get("/")
async def root_get():
    return {"status": "bot is running", "path": "/"}

@app.post("/")
async def root_post(request: Request):
    return await catch_all("", request)

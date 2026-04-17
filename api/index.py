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

# --- Catch-all handler for debugging ---
if dp:
    @dp.message()
    async def match_all_handler(message: types.Message):
        """Matches everything to prove the bot can hear and speak."""
        logger.info(f"MATCH ALL hit by {message.chat.id}")
        await message.answer(f"I HEAR YOU! Your ID: {message.chat.id}. Message was: {message.text}")

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
        return {"ok": False, "error": str(e)}

@app.get("/api/test_msg")
async def test_msg(chat_id: int):
    """
    Directly tests if the bot can send a message.
    """
    try:
        await bot.send_message(chat_id=chat_id, text="🚀 TEST MESSAGE FROM VERCEL")
        return {"ok": True, "message": "Test sent"}
    except Exception as e:
        return {"ok": False, "error": str(e)}

@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(path_name: str, request: Request):
    if request.method == "POST":
        return await process_update(request)
    
    if path_name == "api/check":
        try:
            me = await bot.get_me() if bot else "Not Init"
            return {
                "status": "ok",
                "bot": me.username if not isinstance(me, str) else me,
                "token_prefix": BOT_TOKEN[:10] if BOT_TOKEN else "none"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}

    return {"status": "bot is running", "path": path_name}

@app.get("/")
async def root_get():
    return {"status": "bot is running", "at": "root"}

@app.post("/")
async def root_post(request: Request):
    return await process_update(request)

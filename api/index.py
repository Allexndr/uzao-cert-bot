import os
import sys
import logging
import asyncio
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
from bot import dp, bot
from config import BOT_TOKEN

app = FastAPI()

@app.get("/")
async def index():
    return {"status": "bot is running", "path": "/"}

@app.post("/")
async def webhook_handler(request: Request):
    """
    Simpler webhook handler to ensure basic responsiveness.
    """
    try:
        data = await request.json()
        logger.info(f"Update received: {data}")
        
        # Hydrate the Update object
        update = types.Update(**data)
        
        # Feed the update into the dispatcher
        # Passing bot here is critical for context
        await dp.feed_update(bot, update)
        
        return {"ok": True}
    except Exception as e:
        logger.error(f"Error handling update: {e}", exc_info=True)
        return Response(content=str(e), status_code=200) # Always 200 to stop Telegram retries if we have a bug

# Optional: Health check route that also verifies bot connection
@app.get("/api/health")
async def health():
    try:
        me = await bot.get_me()
        return {"status": "ok", "bot": me.username}
    except Exception as e:
        return {"status": "error", "error": str(e)}

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
from bot import dp, bot
from config import BOT_TOKEN

app = FastAPI()

# Function to process updates
async def process_update(request: Request):
    try:
        data = await request.json()
        logger.info(f"Update received: {data}")
        update = types.Update.model_validate(data, context={"bot": bot})
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        logger.error(f"Error handling update: {e}", exc_info=True)
        # return 200 even on error to stop Telegram from retrying 
        return {"ok": False, "error": str(e)}

@app.get("/")
async def health_root():
    return {"status": "bot is running", "path": "/"}

@app.post("/")
async def webhook_root(request: Request):
    return await process_update(request)

# Catch-all for common webhook paths to avoid 404
@app.post("/api/webhook")
async def webhook_legacy(request: Request):
    return await process_update(request)

@app.get("/api/health")
async def health_api():
    try:
        me = await bot.get_me()
        return {"status": "ok", "bot": me.username}
    except Exception as e:
        return {"status": "error", "error": str(e)}

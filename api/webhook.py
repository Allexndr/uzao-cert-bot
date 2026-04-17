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

from bot import dp, bot
from config import BOT_TOKEN

app = FastAPI()

@app.get("/")
async def index():
    return {"status": "bot is running"}

@app.post("/")
async def webhook_handler(request: Request):
    """
    Handle incoming Telegram updates via Vercel.
    """
    try:
        # Get JSON from request
        data = await request.json()
        logger.info(f"Received update: {data}")
        
        # In aiogram 3.x, we should use model_validate or feed the dict
        # Simple feed_update handles the dict converted to Update
        update = types.Update.model_validate(data, context={"bot": bot})
        
        # Feed the update into the dispatcher
        await dp.feed_update(bot, update)
        
        return {"ok": True}
    except Exception as e:
        logger.error(f"Error processing update: {e}", exc_info=True)
        return Response(content=str(e), status_code=500)

@app.get("/api/set_webhook")
async def set_webhook():
    """
    Utility endpoint to manually reset the webhook.
    """
    webhook_url = f"https://{os.getenv('VERCEL_URL', 'uzao-cert-bot.vercel.app')}/api/webhook"
    result = await bot.set_webhook(webhook_url)
    return {"ok": result, "url": webhook_url}

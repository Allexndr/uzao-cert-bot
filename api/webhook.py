import os
import sys
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types

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
    Handle incoming Telegram updates.
    """
    try:
        # Get JSON from request
        data = await request.json()
        # Feed the update into the dispatcher
        update = types.Update(**data)
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        print(f"Error processing update: {e}")
        return {"error": str(e)}, 500

# Vercel needs the 'app' variable to be exposed at the top level.
# Since app = FastAPI() is at the top level, it should find it.

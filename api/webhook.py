import os
import sys
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

# Add the parent directory to sys.path so we can import our modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from bot import dp, bot
from config import BOT_TOKEN

async def handle_webhook(request):
    """
    Vercel entry point for the Telegram webhook.
    """
    # This is a bit of a hack because Vercel handles the event loop and request lifecycle differently.
    # We use aiogram's SimpleRequestHandler to feed the update into the dispatcher.
    
    # We expect a POST request with the Telegram update.
    if request.method == "POST":
        update_data = await request.json()
        update = Update(**update_data)
        await dp.feed_update(bot, update)
        return web.Response(text="ok")
    
    return web.Response(text="Bot is running!")

# For Vercel, we need a WSGI/ASGI compatible app or a specific function.
# However, Vercel's Python runtime can handle aiohttp-like apps if we provide an entry point.
# But a simpler way for Vercel is to use the standard "handler" function.

async def handler(request):
    # This is the function Vercel calls
    return await handle_webhook(request)

# Note: In a real Vercel environment, we might need to handle the event loop carefully.
# aiogram 3.x is highly async.

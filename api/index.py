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
# We import inside the handler to speed up Lambda cold start if needed, 
# but for now we keep them at module level for simplicity.
try:
    from bot import dp, bot
    from config import BOT_TOKEN
except Exception as e:
    logger.error(f"Critical import error: {e}")
    # Define skeletons to avoid crashes on startup
    dp = None
    bot = None

app = FastAPI()

async def process_update(request: Request):
    if dp is None or bot is None:
        return {"error": "Bot not initialized"}, 500
    
    try:
        data = await request.json()
        logger.info(f"Update received: {data}")
        
        update = types.Update.model_validate(data, context={"bot": bot})
        await dp.feed_update(bot, update)
        return {"ok": True}
    except Exception as e:
        logger.error(f"Error handling update: {e}", exc_info=True)
        return {"ok": False, "error": str(e)}

@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(path_name: str, request: Request):
    """
    Catch-all route to handle traffic regardless of the path Vercel provides.
    """
    logger.info(f"Catch-all hit: {request.method} {path_name}")
    
    if request.method == "POST":
        return await process_update(request)
    
    # For GET requests, return health info
    return {
        "status": "ready",
        "bot_initialized": bot is not None,
        "path_received": path_name,
        "method": request.method
    }

# Also handle the true root
@app.get("/")
async def root_get():
    return {"status": "bot is running", "at": "root"}

@app.post("/")
async def root_post(request: Request):
    return await process_update(request)

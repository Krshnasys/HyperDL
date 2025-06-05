import asyncio
import os
from dotenv import load_dotenv
from pyrogram import Client
from hypertgdownloader import HyperTGDownloader

async def progress_callback(current, total, message_id, *args):
    percentage = (current / total) * 100
    print(f"Message {message_id}: {percentage:.2f}% ({current:,} / {total:,} bytes)")

async def main():
    load_dotenv()
    api_id = os.getenv("TELEGRAM_API_ID")
    api_hash = os.getenv("TELEGRAM_API_HASH")
    bot_token = os.getenv("BOT_1_TOKEN")
    chat_id = int(os.getenv("CHAT_ID", 123456))
    
    if not all([api_id, api_hash, bot_token]):
        raise ValueError("Missing Telegram API credentials in .env file")

    helper_bots = {"bot1": Client("bot1", api_id=api_id, api_hash=api_hash, bot_token=bot_token)}
    helper_loads = {k: 0 for k in helper_bots}

    async with helper_bots["bot1"]:
        downloader = HyperTGDownloader(helper_bots=helper_bots, helper_loads=helper_loads, download_dir="my_downloads/")
        await downloader.start()

        try:
            # Fetch recent messages with media
            messages = []
            async for message in helper_bots["bot1"].get_chat_history(chat_id, limit=10):
                if getattr(message, "media", None):
                    messages.append(message)

            # Download each media file
            for message in messages:
                try:
                    file_path = await downloader.download_media(
                        message=message,
                        file_name=f"my_downloads/message_{message.id}.mp4",
                        progress=lambda c, t: progress_callback(c, t, message.id)
                    )
                    if file_path:
                        print(f"Message {message.id}: Downloaded to {file_path}")
                    else:
                        print(f"Message {message.id}: Download failed or cancelled")
                except Exception as e:
                    print(f"Message {message.id}: Error: {e}")
        except Exception as e:
            print(f"Error fetching messages: {e}")

if __name__ == "__main__":
    asyncio.run(main())
  

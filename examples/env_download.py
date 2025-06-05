import asyncio
import os
from dotenv import load_dotenv
from pyrogram import Client
from hypertgdownloader import HyperTGDownloader

async def progress_callback(current, total, *args):
    percentage = (current / total) * 100
    print(f"Downloading: {percentage:.2f}% ({current:,} / {total:,} bytes)")

async def main():
    load_dotenv()  # Load .env file
    helper_bots = {
        "bot1": Client("bot1", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"), bot_token=os.getenv("BOT_1_TOKEN")),
    }
    helper_loads = {k: 0 for k in helper_bots}

    async with helper_bots["bot1"]:
        downloader = HyperTGDownloader(helper_bots=helper_bots, helper_loads=helper_loads)
        await downloader.start()
        try:
            message = await helper_bots["bot1"].get_messages(
                chat_id=int(os.getenv("CHAT_ID")), message_ids=int(os.getenv("MESSAGE_ID"))
            )
            file_path = await downloader.download_media(
                message=message,
                file_name="my_downloads/env_download.mp4",
                progress=progress_callback
            )
            print(f"Downloaded to: {file_path}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())

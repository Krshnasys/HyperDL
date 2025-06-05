import asyncio
from pyrogram import Client
from hypertgdownloader import HyperTGDownloader

async def main():
    helper_bots = {
        "bot1": Client("bot1", bot_token="YOUR_BOT_1_TOKEN"),
        "bot2": Client("bot2", bot_token="YOUR_BOT_2_TOKEN"),
        # Add more as needed
    }
    main_bot = Client("main_bot", bot_token="YOUR_MAIN_BOT_TOKEN")
    async with main_bot, helper_bots["bot1"], helper_bots["bot2"]:
        downloader = HyperTGDownloader(helper_bots=helper_bots, main_client=main_bot)
        # Get your message object here, e.g. with filters or handlers
        # message = ...
        # path = await downloader.download(message)
        # print(f"Downloaded to {path}")

if __name__ == "__main__":
    asyncio.run(main())

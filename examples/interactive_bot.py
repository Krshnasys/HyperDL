import asyncio
from pyrogram import Client, filters
from hypertgdownloader import HyperTGDownloader

async def main():
    helper_bots = {
        "bot1": Client("bot1", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOUR_BOT_1_TOKEN"),
    }
    main_bot = Client("main_bot", api_id="YOUR_API_ID", api_hash="YOUR_API_HASH", bot_token="YOUR_MAIN_BOT_TOKEN")
    helper_loads = {k: 0 for k in helper_bots}

    downloader = HyperTGDownloader(helper_bots=helper_bots, helper_loads=helper_loads)

    @main_bot.on_message(filters.command("download") & filters.media)
    async def download_command(client, message):
        try:
            file_path = await downloader.download_media(
                message=message,
                file_name=f"my_downloads/{message.id}.mp4",
                progress=lambda c, t: print(f"Progress: {c/t*100:.2f}%")
            )
            await message.reply(f"Downloaded to: {file_path}")
        except Exception as e:
            await message.reply(f"Error: {e}")

    async with main_bot, helper_bots["bot1"]:
        await downloader.start()
        await main_bot.start()
        print("Bot is running. Send /download with a media message.")
        await asyncio.Event().wait()  # Keep bot running

if __name__ == "__main__":
    asyncio.run(main())

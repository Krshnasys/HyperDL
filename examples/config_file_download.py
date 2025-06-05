import asyncio
import json
import os
from pyrogram import Client
from hypertgdownloader import HyperTGDownloader

async def progress_callback(current, total, *args):
    percentage = (current / total) * 100
    print(f"Downloading: {percentage:.2f}% ({current:,} / {total:,} bytes)")

async def main():
    # Load config from JSON file
    config_path = "config.json"
    if not os.path.exists(config_path):
        raise FileNotFoundError("config.json not found. Create it with API credentials.")

    with open(config_path, "r") as f:
        config = json.load(f)

    api_id = config["telegram"]["api_id"]
    api_hash = config["telegram"]["api_hash"]
    bot_tokens = config["telegram"]["bot_tokens"]

    helper_bots = {
        f"bot{i+1}": Client(f"bot{i+1}", api_id=api_id, api_hash=api_hash, bot_token=token)
        for i, token in enumerate(bot_tokens)
    }
    helper_loads = {k: 0 for k in helper_bots}

    async with helper_bots["bot1"], helper_bots.get("bot2"):
        downloader = HyperTGDownloader(
            helper_bots=helper_bots,
            helper_loads=helper_loads,
            num_parts=config.get("download", {}).get("num_parts", 8),
            download_dir=config.get("download", {}).get("download_dir", "my_downloads/")
        )
        await downloader.start()

        try:
            message = await helper_bots["bot1"].get_messages(
                chat_id=config["telegram"]["chat_id"],
                message_ids=config["telegram"]["message_id"]
            )
            file_path = await downloader.download_media(
                message=message,
                file_name=f"{config['download']['download_dir']}/config_download.mp4",
                progress=progress_callback,
                dump_chat=config["telegram"].get("dump_chat_id")
            )
            if file_path:
                print(f"Downloaded to: {file_path}")
            else:
                print("Download was cancelled or failed.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())

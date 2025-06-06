# HyperDL: Superfast Telegram Downloader Library for Pyrogram Bots

**HyperDL** is a parallel, multi-bot download engine for Pyrogram bots, designed for ultra-fast Telegram file downloads.  
Replace slow `.download()` with HyperDL and unleash full speed using helper bots!

---

## Features

- **Blazing fast**: Download files in parallel using multiple helper bots.
- **Plug-and-play**: Drop into any Pyrogram bot—watermark bots, renamer bots, leech bots, and more.
- **No core code changes needed**: Use `HyperTGDownloader` as a drop-in replacement for Pyrogram’s download system.
- **Works for all media types**: Documents, videos, audio, etc.
- **Handles large files**: Bypass Telegram’s rate limits by splitting downloads.

---

## Requirements

- Python 3.8+
- [pyrogram](https://docs.pyrogram.org/) v2+
- [tgcrypto](https://github.com/pyrogram/tgcrypto)
- At least **one main bot** and **one or more helper bots** (@BotFather bots)
- A **dump chat** (private/group/channel, all your helper bots and main bot must be admins)

---

## Quickstart Example

1. **Install dependencies:**
    ```sh
    pip install pyrogram tgcrypto
    ```

2. **Setup your `config.py`:**
    ```python
    class Config:
        API_ID = 123456          # from https://my.telegram.org
        API_HASH = "your_api_hash"
        BOT_TOKEN = "main_bot_token"
        HELPER_TOKENS = "helper1_token helper2_token"  # space-separated tokens
        LEECH_DUMP_CHAT = -1001234567890  # your dump chat/channel ID
        DOWNLOAD_DIR = "downloads/"
        HYPER_THREADS = 8
        CHUNK_SIZE = 1024 * 1024  # 1MB
    ```

3. **Basic bot integration:**
    ```python
    import asyncio
    from pyrogram import Client, filters, idle
    from config import Config
    from hypertgdownloader import HyperTGDownloader

    # Setup helper bots
    helper_bots = {}
    for i, token in enumerate(Config.HELPER_TOKENS.split()):
        helper_bots[i] = Client(
            f"helper_{i}",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=token,
            in_memory=True
        )
    helper_loads = {i: 0 for i in helper_bots}

    # Hyper downloader
    downloader = HyperTGDownloader(
        helper_bots=helper_bots,
        helper_loads=helper_loads,
        num_parts=Config.HYPER_THREADS,
        chunk_size=Config.CHUNK_SIZE,
        download_dir=Config.DOWNLOAD_DIR,
    )

    main_bot = Client(
        "main_bot",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        in_memory=True
    )

    @main_bot.on_message(filters.command("dl") & filters.reply)
    async def download_handler(client, message):
        replied = message.reply_to_message
        if not replied:
            await message.reply(" Reply to a media message with /dl.")
            return
        msg = await message.reply(" Downloading, please wait...")
        try:
            file_path = await downloader.download_media(
                replied,
                file_name=Config.DOWNLOAD_DIR,
                progress=None,
                progress_args=(),
                dump_chat=Config.LEECH_DUMP_CHAT
            )
            if file_path:
                await msg.edit_text(f"Download complete:\n<code>{file_path}</code>")
            else:
                await msg.edit_text("Download failed or cancelled.")
        except Exception as e:
            await msg.edit_text(f" Error: {e}")

    async def main():
        await asyncio.gather(*(bot.start() for bot in helper_bots.values()))
        await main_bot.start()
        await downloader.start()
        print("All bots started. Send /dl as a reply to a media message.")
        await idle()

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(main())
        finally:
            loop.run_until_complete(main_bot.stop())
            for bot in helper_bots.values():
                loop.run_until_complete(bot.stop())
            loop.close()
    ```

---

## Usage in Any Pyrogram Bot

Replace:
```python
await message.download()
```
with:
```python
await downloader.download_media(message, file_name="downloads/", dump_chat=LEECH_DUMP_CHAT)
```
- You can use all HyperDL features in watermark bots, video samplers, metadata editors, renamers, and more.

---

## Tips

- **All helper bots AND main bot must be admins in the dump chat!**
- **Your dump chat can be a private group, channel, or supergroup.**
- Adjust `HYPER_THREADS` and `CHUNK_SIZE` for maximum speed according to server/network.

---
## License
[MIT](https://opensource.org/licenses/MIT).

---

## Special Thanks ♥️

- [Pyrogram](https://github.com/pyrogram/pyrogram)  
- [SilentDemonSD](https://github.com/SilentDemonSD)

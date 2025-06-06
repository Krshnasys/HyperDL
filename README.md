[![PyPI version](https://badge.fury.io/py/hypertgdownloader.svg)](https://pypi.org/project/hypertgdownloader/)
[![Downloads](https://pepy.tech/badge/hypertgdownloader)](https://pepy.tech/project/hypertgdownloader)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# HyperDL: Superfast Telegram Downloader Library for Pyrogram Bots

```bash
pip install hypertgdownloader
```

**HyperDL** is a parallel, multi-bot download engine for Pyrogram bots, designed for ultra-fast Telegram file downloads.  
Replace slow `.download()` with HyperDL and unleash full speed using helper bots!

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
- You can use HyperDL in any Pyrogram-based bots
---

## Nots 

- **All helper bots AND main bot must be admins in the dump chat!**
- **Your dump chat can be a private group, channel, or supergroup.**
- Adjust `HYPER_THREADS` and `CHUNK_SIZE` for maximum speed according to server/network.

---

## Real Author ♥️♥️

- [Pyrogram](https://github.com/pyrogram/pyrogram)  
- [SilentDemonSD](https://github.com/SilentDemonSD)
- 

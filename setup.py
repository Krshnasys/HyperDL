from setuptools import setup, find_packages

setup(
    name="hypertgdownloader",
    version="0.1.0",
    description="High-speed Telegram downloader using multiple helper bots (Pyrogram)",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pyrogram>=2.0.0",
        "aiofiles",
    ],
    python_requires=">=3.8",
)
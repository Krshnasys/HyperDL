from setuptools import setup, find_packages

setup(
    name="hypertgdownloader", 
    version="0.1.0",  
    description="High-speed Telegram downloader using multiple helper bots",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Krshnasys",  
    url="https://github.com/Krshnasys/HyperDL",  
    packages=find_packages(),
    install_requires=[
        "pyrogram>=2.0.0",
        "aiofiles",
        "aioshutil",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        "hypertgdownloader": ["examples/*.py"],
    },
)

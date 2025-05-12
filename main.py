import asyncio
from scanner import scan_comments
from triggers import load_blacklist

ASCII_ART = r"""
 ____    ___   ___  ____   _  __  ____   ___  ____    ___   ____      _     ____    ___  __     __
|  _ \  / _ \ |_ _|/ ___| | |/ / |  _ \ |_ _||  _ \  / _ \ |  _ \    / \   / ___|  / _ \ \ \   / /
| |_) || | | | | | \___ \ | ' /  | |_) | | | | | | || | | || |_) |  / _ \  \___ \ | | | | \ \ / /
|  __/ | |_| | | |  ___) || . \  |  __/  | | | |_| || |_| ||  _ <  / ___ \  ___) || |_| |  \ V /
|_|     \___/ |___||____/ |_|\_\ |_|    |___||____/  \___/ |_| \_\_/   \_\|____/  \___/    \_/

              YTScanner (Lite Edition)
"""

if __name__ == "__main__":
    print(ASCII_ART)
    video_link = input("URL: ").strip()
    blacklist = load_blacklist()
    asyncio.run(scan_comments(video_link, blacklist))

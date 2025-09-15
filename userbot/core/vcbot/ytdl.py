# Zed - UserBot
# Copyright (c) 2022 ZED_USERBOT
# Credits: @ZedThon || https://github.com/ZedThon
#
# This file is a part of < https://github.com/ZedThon/ZED_USERBOT/ >
# t.me/ZedThon & t.me/zzzzl1l

from youtubesearchpython import VideosSearch

from userbot import LOGS
from userbot.helpers import bash


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = data["thumbnails"][0]["url"]
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        LOGS.info(str(e))
        return 0


async def ytdl(link: str):
    stdout, stderr = await bash(
        f'yt-dlp -g -f "best[height<=?720][width<=?1280]" {link}'
    )
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr

#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
# Port to UserBot
# modified by @ZedThon
# Copyright (C) 2022.

import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


try:
    pass
except:
    os.system("pip install instantmusic")


os.system("rm -rf *.mp3")


def bruh(name):

    os.system("instantmusic -q -s " + name)


@zedthon.on(admin_cmd(pattern="ريماكس ?(.*)"))

async def remaxzedthon(zedrm):
    ok = zedrm.pattern_match.group(1)
    if not ok:
        if zedrm.is_reply:
            what = (await zedrm.get_reply_message()).message
        else:
            await zedrm.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "spotifybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(zedrm.chat_id,
                            reply_to=zedrm.reply_to_msg_id,
                            silent=True if zedrm.is_reply else False,
                            hide_via=True)
    await zedrm.delete()
    

@borg.on(admin_cmd(pattern="ريمكس ?(.*)"))
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    zelzal = "@spotifybot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()


@zedthon.on(admin_cmd(pattern="^.dzd(?: |$)(.*)", outgoing=True))
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await Deezlod.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await Deezlod.edit("**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await Deezlod.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
            return
        await bot.send_file(Deezlod.chat_id, song, caption=details.text)
        await Deezlod.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )
        await Deezlod.delete()


#𝙕𝙚𝙙𝙏𝙝𝙤𝙣 ®
# Port to UserBot
# modified by @ZedThon
# Copyright (C) 2022.

import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *

@zedthon.on(zelzal_cmd(pattern="ساوند$", outgoing=True))
@zedthon.on(sudo_cmd(pattern="ساوند$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```بالـرد على الرابـط حمبـي 🧸🎈```**")
        return
    chat = "@DeezerMusicBot"
    catevent = await edit_or_reply(event, "**╮ ❐ جـارِ التحميـل من سـاوند كـلاود انتظـر قليلاً  ▬▭... 𓅫╰**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=595898211)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "**❈╎تحـقق من انـك لم تقـم بحظـر البوت @downloader_tiktok_bot .. ثم اعـد استخدام الامـر ...🤖♥️**"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("**🤨💔...؟**")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@borg.on(zelzal_cmd(pattern="كلود ?(.*)"))
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    zelzal = "@DeezerMusicBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(zelzal, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()


CMD_HELP.update(
    {
        "ساوند كلاود": "**اسم الاضافـه : **`ساوند كلاود`\
    \n\n**╮•❐ الامـر ⦂ **`.كلود` + اسـم الاغنيـه\
    \n**الشـرح •• **بحث وتحميل الاغـاني من سـاوند كـلاود\
    \n\n**╮•❐ الامـر ⦂ **`.ساوند` بالرد على الرابط\
    \n**الشـرح •• **تحميل مقاطـع الفيديـو من سـاوند كـلاود"
    }
)

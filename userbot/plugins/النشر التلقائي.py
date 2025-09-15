from telethon import *
from userbot.plugins.sql_helper.autopost_sql import add_post, get_all_post, is_post, remove_post
from . import BOTLOG, get_user_from_event
from . import *

@zedthon.on(admin_cmd(pattern="نشر_تلقائي ?(.*)"))
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        zed = str(trz_).replace("-100", "")
    else:
        zed = trz_
    if not zed.isdigit():
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بوضـع ايـدي القنـاة اولاً**")
    if is_post(zed , event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تفعيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    add_post(zed, event.chat_id)
    await edit_or_reply(event, f"**✾╎جـاري بدء النشـر التلقـائي من القنـاة ** `{trz_}`")


@zedthon.on(admin_cmd(pattern="ايقاف_النشر ?(.*)"))
async def _(event):
    if (event.is_private or event.is_group):
        return await edit_or_reply(event, "**✾╎عـذراً .. النشر التلقائي خـاص بالقنـوات فقـط**")
    trz_ = event.pattern_match.group(1)
    if str(trz_).startswith("-100"):
        zed = str(trz_).replace("-100", "")
    else:
        zed = trz_
    if not zed.isdigit():
        return await edit_or_reply(event, "**✾╎عـذراً .. قـم بوضـع ايـدي القنـاة اولاً**")
    if not is_post(zed, event.chat_id):
        return await edit_or_reply(event, "**✾╎تم تعطيـل النشر التلقـائي لهـذه القنـاة هنـا .. بنجـاح ✓**")
    remove_post(zed, event.chat_id)
    await edit_or_reply(event, f"**✾╎تم ايقـاف النشـر التلقـائي من** `{trz_}`")


@zedthon.on(admin_cmd(incoming=True))
async def _(event):
    if event.is_private:
        return
    chat_id = str(event.chat_id).replace("-100", "")
    channels_set  = get_all_post(chat_id)
    if channels_set == []:
        return
    for chat in channels_set:
        if event.media:
            await event.client.send_file(int(chat), event.media, caption=event.text)
        elif not event.media:
            await bot.send_message(int(chat), event.message)


CMD_HELP.update(
    {
        "النشر التلقائي": "**اسم الاضافـه : **`النشر التلقائي`\
    \n\n**╮•❐ الامـر ⦂ **`.نشر_تلقائي` + ايدي القناة اللي تريد تاخذ منها نشر\
    \n**الشـرح •• **اذهـب لقناتك اللي تريدها تسحب منشورات تلقائي وارسل الامر\
    \n\n**╮•❐ الامـر ⦂ **`.ايقاف_النشر` + ايدي نفس القناة بالامر السابق\
    \n**الشـرح •• **لـ ايقـاف النشـر التلقائـي"
    }
)
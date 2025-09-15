from telethon import events

from . import * 

ZED_BLACKLIST = [
    -1001236815136,
    -1001614012587,
    ]
#

@zedthon.on(zelzal_cmd(pattern=f"للمجموعات(?: |$)(.*)"))
async def gcast(event):
    zedthon = event.pattern_match.group(1)
    if zedthon:
        msg = zedthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await eor(event, "**✾╎بالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**")
        return
    roz = await edit_or_reply(event, "**✾╎ جـاري الاذاعـه في المجموعـات ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in ZED_BLACKLIST:
                    await event.client.send_message(chat, msg)
                    done += 1
            except BaseException:
                er += 1
    await roz.edit(
        f"**✾╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من المجموعـات ، خطـأ في الارسـال الـى ** `{er}` **من المجموعـات**"
    )
    
@zedthon.on(zelzal_cmd(pattern=f"للخاص(?: |$)(.*)"))
async def gucast(event):
    zedthon = event.pattern_match.group(1)
    if zedthon:
        msg = zedthon
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        await eor(event, "**✾╎بالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**")
        return
    roz = await edit_or_reply(event, "**✾╎ جـاري الاذاعـه في الخـاص ...الرجـاء الانتظـار**")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            try:
                done += 1
                await event.client.send_message(chat, msg)
            except BaseException:
                er += 1
    await roz.edit(
        f"**✾╎تمت الاذاعـه بنجـاح الـى ** `{done}` **من الخـاص ، خطـأ في الارسـال الـى ** `{er}` **من الخـاص**"
    )
    

@zedthon.on(zelzal_cmd(pattern="خاص ?(.*)"))
async def pmto(event):
    r = event.pattern_match.group(1)
    p = r.split(" ")
    chat_id = p[0]
    try:
        chat_id = int(chat_id)
    except BaseException:
        pass
    msg = ""
    for i in p[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await borg.send_message(chat_id, msg)
        await event.edit("**✾╎تـم ارسال الرسـالة الـى الشخـص بـدون الدخـول للخـاص .. بنجـاح ✓**")
    except BaseException:
        await event.edit("**✾╎اووبس .. لقـد حدث خطـأ مـا .. اعـد المحـاوله**")


CMD_HELP.update(
    {
        "الاذاعه": "**اسم الاضافـه : **`الاذاعه`\
    \n\n**╮•❐ الامـر ⦂ **`.للمجموعات` \nبالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**\
    \n**الشـرح •• **اذاعـة رسـالة او ميديـا لكـل المجموعـات اللي انت موجود فيهـا \
    \n\n**╮•❐ الامـر ⦂ **`.للخاص` \nبالـرد ؏ــلى رسـالة او وسائـط او كتابـة رسـالة مع الامـࢪ**\
    \n**الشـرح •• **اذاعـه رسـاله او ميديـا لكـل الاشخـص الموجودين معاك خاص\
    \n\n**╮•❐ الامـر ⦂ **`.خاص` + معرف الشخص + الرسـاله\
    \n**الشـرح •• **ارسـال رسـاله الى الشخص المحدد بدون الدخول للخاص وقراءة الرسـائل"
    }
)

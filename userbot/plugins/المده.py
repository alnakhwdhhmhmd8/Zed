"""
©Zed : @ZedThon
  - zed UpTime
  - Commend: .المده
"""

import time

from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "ZEDbot"
ZED_IMG = "https://telegra.ph/file/4c406eb5e6932d4834947.jpg"
ZED_TEXT = "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𓆪"
ZEDEM = "**⌔∮**"


@bot.on(admin_cmd(outgoing=True, pattern="المده$"))
@bot.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptzed(zed):
    if zed.fwd_from:
        return
    zedid = await reply_id(zed)
    zedupt = await get_readable_time((time.time() - StartTime))
    if ZED_IMG:
        zed_c = f"**{ZED_TEXT}**\n"
        zed_c += f"**{ZEDEM} المستخدم :** {mention}\n"
        zed_c += f"**{ZEDEM} مدة التشغيل :** `{zedupt}`"
        await zed.client.send_file(zed.chat_id, ZED_IMG, caption=zed_c, reply_to=zedid)
        await zed.delete()
    else:
        await edit_or_reply(
            zed,
            f"**{ZED_TEXT}**\n\n"
            f"**{ZEDEM} المستخدم :** {mention}\n"
            f"**{ZEDEM} مدة التشغيل :** `{zedupt}`",
        )

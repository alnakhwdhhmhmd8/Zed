"""
©Zed : @ZedThon
  - Tumblr Gif -1
  - Tumblr Gif -2
  - Tumblr Gif -3
  - Tumblr Gif -4
  - Tumblr Gif -5
  - Tumblr Gif -6
  - Tumblr Gif -7

"""


from .. import reply_id as rd 
from . import *

@bot.on(admin_cmd(outgoing=True, pattern="ت1$"))
@bot.on(sudo_cmd(pattern="ت1$", allow_sudo=True))
async def tmgif(zel):
    if zel.fwd_from:
        return
    zelid = await rd(zel)
    if tm_gif:
        zel_c = f"**{TMTE}**\n"
        zel_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        zel_c += f"**↫ المتـحركه الاولى 𓆰.**"
        await zel.client.send_file(zel.chat_id, tm_gif, caption=zel_c, reply_to=zelid)


@bot.on(admin_cmd(outgoing=True, pattern="ت2$"))
@bot.on(sudo_cmd(pattern="ت2$", allow_sudo=True))
async def tmgif(lon):
    if lon.fwd_from:
        return
    lonid = await rd(lon)
    if tm_gif2:
        ics_c = f"**{TMTE}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الثانيه 𓆰.**"
        await lon.client.send_file(lon.chat_id, tm_gif2, caption=ics_c, reply_to=lonid)


@bot.on(admin_cmd(outgoing=True, pattern="ت3$"))
@bot.on(sudo_cmd(pattern="ت3$", allow_sudo=True))
async def tmgif(i):
    if i.fwd_from:
        return
    sic_id = await rd(i)
    if tm_gif3:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الثالثه 𓆰.**"
        await i.client.send_file(i.chat_id, tm_gif3, caption=tumc, reply_to=sic_id)


@bot.on(admin_cmd(outgoing=True, pattern="ت4$"))
@bot.on(sudo_cmd(pattern="ت4$", allow_sudo=True))
async def tmgif(lon):
    if lon.fwd_from:
        return
    reply_to_id = await rd(lon)
    if tm_gif4:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await lon.client.send_file(
            lon.chat_id, tm_gif4, caption=tumc, reply_to=reply_to_id
        )


@bot.on(admin_cmd(outgoing=True, pattern="ت5$"))
@bot.on(sudo_cmd(pattern="ت5$", allow_sudo=True))

async def tmgif(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if tm_gif5:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الخامسه 𓆰.**"
        await zed.client.send_file(
            zed.chat_id, tm_gif5, caption=tumc, reply_to=reply_to_id
        )


@bot.on(admin_cmd(outgoing=True, pattern="ت6$"))
@bot.on(sudo_cmd(pattern="ت6$", allow_sudo=True))

async def tmgif(zelzal):
    if zelzal.fwd_from:
        return
    reply_to_id = await rd(zelzal)
    if tm_gif6:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه السادسه 𓆰.**"
        await zelzal.client.send_file(
            zelzal.chat_id, tm_gif6, caption=tumc, reply_to=reply_to_id
        )


@bot.on(admin_cmd(outgoing=True, pattern="ت7$"))
@bot.on(sudo_cmd(pattern="ت7$", allow_sudo=True))
async def tmgif(zed):
    if zed.fwd_from:
        return
    reply_to_id = await rd(zed)
    if tm_gif7:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧℤ𝔼𝔻𝕋ℍ𝕆ℕⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه السابعه 𓆰.**"
        await zed.client.send_file(
            zed.chat_id, tm_gif7, caption=tumc, reply_to=reply_to_id
        )

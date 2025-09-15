# animation code for zed edit by @zlzzl77

import asyncio
from collections import deque


@bot.on(admin_cmd(pattern="افكر$", outgoing=True))
@bot.on(sudo_cmd(pattern="افكر$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, ".🧐")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"متت$"))
@bot.on(sudo_cmd(pattern="متت$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, ".🤣")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"ضايج$"))
@bot.on(sudo_cmd(pattern="ضايج$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🙂.")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="ساعه$"))
@bot.on(sudo_cmd(pattern="ساعه$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🕙.")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"مح$"))
@bot.on(sudo_cmd(pattern="مح$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "😗.")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="قلب$"))
@bot.on(sudo_cmd(pattern="قلب$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🧡.")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="جيم$", outgoing=True))
@bot.on(sudo_cmd(pattern="جيم$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "جيم")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"الارض$", outgoing=True))
@bot.on(sudo_cmd(pattern="الارض$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🌏.")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="قمر$"))
@bot.on(sudo_cmd(pattern="قمر$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🌗.")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"اقمار$", outgoing=True))
@bot.on(sudo_cmd(pattern="اقمار$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🌗.")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("⇆")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern=f"قمور$", outgoing=True))
@bot.on(sudo_cmd(pattern="قمور$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "قمور..")
    animation_interval = 0.1
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


CMD_HELP.update(
    {
        "تسليه2": """**Plugin : **`تسليه2`
        
**Commands in animation2 are **
  •  `.افكر`
  •  `.متت`
  •  `.ضايج`
  •  `.ساعه`
  •  `.مح`
  •  `.قلب`
  •  `.جيم`
  •  `.الارض`
  •  `.قمر`
  •  `.اقمار`
  •  `.قمور`
  
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)

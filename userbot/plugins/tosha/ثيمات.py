"""
©Zed : @ZedThon
  - Commends of All Theme
"""

from . import *

@bot.on(admin_cmd(pattern="م30"))
@bot.on(sudo_cmd(pattern="م30", allow_sudo=True))
async def zed(zelzal):
    await eor(zelzal, X)

@bot.on(admin_cmd(pattern="ثيمات"))
@bot.on(sudo_cmd(pattern="ثيمات", allow_sudo=True))
async def zed(zelzal):
    await eor(zelzal, ZL)



"""
©Zed : @ZedThon
  - Commends of All Wallpapers
"""

from . import *

@bot.on(admin_cmd(pattern="م31"))
@bot.on(sudo_cmd(pattern="م31", allow_sudo=True))
async def zed(zalzal):
    await eor(zalzal, W)

@bot.on(admin_cmd(pattern="خلفيات1"))
@bot.on(sudo_cmd(pattern="خلفيات1", allow_sudo=True))
async def zed(zalzal):
    await eor(zalzal, WL)
    
@bot.on(admin_cmd(pattern="خلفيات2"))
@bot.on(sudo_cmd(pattern="خلفيات2", allow_sudo=True))
async def zed(zalzal):
    await eor(zalzal, BN)



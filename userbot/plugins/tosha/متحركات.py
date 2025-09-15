"""
©Zed : @ZedThon
  - Commends of All Gif
"""

from . import *

@bot.on(admin_cmd(pattern="م20"))
@bot.on(sudo_cmd(pattern="م20", allow_sudo=True))
async def zed(tosh):
    await eor(tosh, T)

@bot.on(admin_cmd(pattern="متحركات تمبلر"))
@bot.on(sudo_cmd(pattern="متحركات تمبلر", allow_sudo=True))
async def zed(tosh):
    await eor(tosh, O)

@bot.on(admin_cmd(pattern="متحركات كيوت"))
@bot.on(sudo_cmd(pattern="متحركات كيوت", allow_sudo=True))
async def zed(tosh):
    await eor(tosh, S)

@bot.on(admin_cmd(pattern="متحركات حب"))
@bot.on(sudo_cmd(pattern="متحركات حب", allow_sudo=True))
async def zed(tosh):
    await eor(tosh, H)

@bot.on(admin_cmd(pattern="متحركات تحشيش"))
@bot.on(sudo_cmd(pattern="متحركات تحشيش", allow_sudo=True))
async def zed(tosh):
    await eor(tosh, A)





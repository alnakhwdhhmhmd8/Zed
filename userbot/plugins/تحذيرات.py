"""
©Zed : @ZedThon
  - Warns Code For Zed
  - Commends: .warn, .warns, .resetwarns
"""
import html

import userbot.plugins.sql_helper.warns_sql as sql


@bot.on(admin_cmd(pattern="تحذير (.*)"))
@bot.on(sudo_cmd(pattern="تحذير (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    warn_reason = event.pattern_match.group(1)
    if not warn_reason:
        warn_reason = "No reason"
    reply_message = await event.get_reply_message()
    limit, soft_warn = sql.get_warn_setting(event.chat_id)
    num_warns, reasons = sql.warn_user(
        reply_message.sender_id, event.chat_id, warn_reason
    )
    if num_warns >= limit:
        sql.reset_warns(reply_message.sender_id, event.chat_id)
        if soft_warn:
            logger.info("TODO: kick user")
            reply = "{} تحذيرات, [user](tg://user?id={}) ادت الى دفـره من الكروب!".format(
                limit, reply_message.sender_id
            )
        else:
            logger.info("TODO: ban user")
            reply = "{} warnings, [user](tg://user?id={}) has to bee banned!".format(
                limit, reply_message.sender_id
            )
    else:
        reply = "[user](tg://user?id={}) يمتلك {}/{} تحذيرات... اكعـد عاقل وليـدي!".format(
            reply_message.sender_id, num_warns, limit
        )
        if warn_reason:
            reply += "\nReason for last warn:\n{}".format(html.escape(warn_reason))
    await edit_or_reply(event, reply)


@bot.on(admin_cmd(pattern="احذر$"))
@bot.on(sudo_cmd(pattern="احذر$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    result = sql.get_warns(reply_message.sender_id, event.chat_id)
    if result and result[0] != 0:
        num_warns, reasons = result
        limit, soft_warn = sql.get_warn_setting(event.chat_id)
        if reasons:
            text = "This user has {}/{} تحذيرات, for the following reasons:".format(
                num_warns, limit
            )
            text += "\r\n"
            text += reasons
            await event.edit(text)
        else:
            await edit_or_reply(
                event,
                "this user has {} / {} warning, but no reasons for any of them.".format(
                    num_warns, limit
                ),
            )
    else:
        await edit_or_reply(event, "this user hasn't got any warnings!")


@bot.on(admin_cmd(pattern="حذف التحذير$"))
@bot.on(sudo_cmd(pattern="حذف التحذير$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    sql.reset_warns(reply_message.sender_id, event.chat_id)
    await edit_or_reply(event, "Warnings have been reset!")


CMD_HELP.update(
    {
        "تحذيرات": "**Plugin : **`تحذيرات`\
    \n\n  •  **Syntax : **`.تحذير + السبب` reply to user\
    \n  •  **Function : **__warns the given user in the chat you used__\
    \n\n  •  **Syntax : **`.احذر بالرد`\
    \n  •  **Function : **__gets the warns of the given user in the chat you used__\
    \n\n  •  **Syntax : **`حذف التحذير بالرد`\
    \n  •  **Function : **__resets the warns of the replied users in the chat where u used command__"
    }
)

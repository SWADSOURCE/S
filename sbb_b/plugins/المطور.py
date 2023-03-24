from telethon import Button, events

from sbb_b import sbb_b 

from ..Config import Config

ROZ_PIC = "https://telegra.ph/file/3fc81ce88a72c6458c664.jpg"
RAZAN = Config.TG_BOT_USERNAME
ROZ_T = (
    f"**مطور سورس أفـاتـار **\n"
  
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("المطور") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("ㅤ𓏺 ძᥱ᥎ ꧑᥆Ꮒᥲ️꧑ᥱძ . 🕷 ˼", "https://t.me/DIV_MUHAMED"),
                    Button.url("𓏺  〝𝘼𝙑⍢⃝𝙎𝙊𝙐𝙍𝘾𝞝〞. 🕷 ˼", "https://t.me/source_av"),
                    Button.url("ㅤ𓏺 H᥆ꪝ T᥆ Bᥱ Cᥣ᥆ꪝꪀ . 🕷 ˼ ", "t.me/S_325"),
                    Button.url("𓏺 Ⴆ᥆ƚ ꧑᥆Ꮒᥲ️꧑ᥱძ . 🕷 ˼", "https://t.me/MarchemlloXx_bot"),
                    
                ]
            ]
            
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ_T, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="JMTHON - sbb_b",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="JMTHON - sbb_b",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@sbb_b.ar_cmd(pattern="المطور")
async def repo(event):
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "المطور")
    await response[0].click(event.chat_id)
    await event.delete()


# edit by ~ @RR77R

from ..helpers.functions.functions import make_inline
from . import edit_delete, reply_id, sbb_b


@sbb_b.ar_cmd(pattern="التنصيب(?:\s|$)([\s\S]*)")
async def _(event):
    reply_to_id = await reply_id(event)
    reply_message = await event.get_reply_message()
    if reply_message:
        markdown_note = reply_message.text
    else:
        markdown_note = "".join(event.text.split(maxsplit=1)[1:])
    if not markdown_note:
        return await edit_delete(event, "**-https://t.me/FTTUTY/270 **")
    await make_inline(markdown_note, event.client, event.chat_id, reply_to_id)
    await event.delete()

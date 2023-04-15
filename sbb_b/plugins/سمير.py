import random

from razan.strings.fun import *
from sbb_b import sbb_b
from sbb_b.core.managers import edit_or_reply
from sbb_b.helpers import get_user_from_event

from . import *


@sbb_b.ar_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بقلبك 🖤 \n وبطل محن كلاب بق 🙄😹 "
    )


@sbb_b.ar_cmd(pattern="رفع خول(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5566753847:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه خول لما يسترجل نزلو 🥱 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة الكلاب 😁 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل خول(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة الخولات 👻 ",
    )


@sbb_b.ar_cmd(pattern="رفع سيمب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه سيمب خلي الحريم تنفعو 😂😂 ",
    )


@sbb_b.ar_cmd(pattern="تنزيل سيمب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة السيمب 🤡 ",
    )


@sbb_b.ar_cmd(pattern="رفع شاذ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم رفعه شاذ لما يسترجل نزلو 🤡",
    )


@sbb_b.ar_cmd(pattern="تنزيل شاذ(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f" - المستخدم [{tag}](tg://user?id={user.id}) \n\n- تم تنزيله من قائمة الشواذ 🙀",
    )


@sbb_b.ar_cmd(pattern="تنزيل بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده في قلب الجميع 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده في قلب الجميع 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f""**- اسكت يمتخلف ده في قلب الجميع 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تم تنزيله من قلبك واصبحت مكسور القلب 🙂💔",
    )


@sbb_b.ar_cmd(pattern="رفع عرص(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه معرص بنجاح 😅",
    )


@sbb_b.ar_cmd(pattern="تنزيل عرص(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم تنزيله من المعرصين 🤣",
    )


@sbb_b.ar_cmd(pattern="رفع متوحد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه متوحد 🙂",
    )


@sbb_b.ar_cmd(pattern="تنزيل متوحد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم تنزيله من قائمة المتوحدين  🤦🏻‍♂️😃",
    )


@sbb_b.ar_cmd(pattern="رفع حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه حمار شوفو حد يربكو 😹",
    )


@sbb_b.ar_cmd(pattern="تنزيل حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5680297831:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور سمير 🙄 **")
    if user.id == 1400467850:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور كينج 🙄**")
    if user.id == 5957205447:
        return await edit_or_reply(mention, f"**- اسكت يمتخلف ده المطور محمد 🙄**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم تنزيله من قائمة الحمير 😂 \n كده مش هنلاقي حد نركبو 🙀",
    )

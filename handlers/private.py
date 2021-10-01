from time import time
from datetime import datetime
from pyrogram import Client, filters
from helpers.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import sudo_users_only

from config import BOT_NAME as bn
from helpers.filters import other_filters2

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
💝Tԋιʂ Iʂ Aԃʋαɳƈҽ Tҽʅҽɠɾαɱ Mυʂιƈ Bσƚ \n⚡Rυɳ Oɳ Pɾιʋαƚҽ VPS Sҽɾʋҽɾ \n🌼Fҽҽʅ Hιɠԋ Qυαʅιƚყ Mυʂιƈ Iɳ Vƈ \n🥀Dҽʋҽʅσρҽԃ Bყ [нｅⒺŇ𝐀Xđ](https://t.me/HEENAXD)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰๏ฬภєг❱", url="https://t.me/XD_LIF")
                  ],[
                    InlineKeyboardButton(
                        "❰Sυρρσɾƚ❱", url="https://t.me/MISTY_SUPORTER"
                    ),
                    InlineKeyboardButton(
                        "❰Gɾσυρ❱", url="https://t.me/L0VEXWORLD"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰Cԋαƚιɳɠ Gɾσυρ❱", url="https://t.me/L0VEXWORLD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **Jαɳʋι Sαɾʋҽɾ ιʂ Rυɳɳιɳɠ**\n<b>✨ **Uρƚιɱҽ:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Gɾσυρ", url=f"https://t.me/L0VEXWORLD"
                    ),
                    InlineKeyboardButton(
                        "📣 Cԋҽɳɳαʅ", url=f"https://t.me/MISTY_SUPORT"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command("ping") & ~filters.private & ~filters.channel)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("℘ıŋŋɠ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "✨`℘ơŋɠ!!`\n"
        f"🤞  `{delta_ping * 1000:.3f} ᴍꜱ`"
    )

@Client.on_message(filters.command("uptime") & ~filters.private & ~filters.channel)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🔥Jαɳʋι Sƚαƚυʂ:\n"
        f"• **ᴜᴘᴛɪᴍᴇ:** `{uptime}`\n"
        f"• **ꜱᴛᴀʀᴛ ᴛɪᴍᴇ:** `{START_TIME_ISO}`"
    )

#zaid Project 
#Ur Motherfucker If U Kang And Don't Give Creadits 🥴

from os import path

from pyrogram import Client, filters
from pyrogram.types import Message

from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


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


@Client.on_message(filters.command(["alive", f"alive@QueenAlishaRobot{BOT_USERNAME}"]))
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_photo(
        photo=f"https://telegra.ph/file/66a1ddb05e34513c226a4.jpg",
        caption=f"""✪✪✪ ʜɪɪ ɪ ᴍ 乛𝘼𝙇𝙄𝙎𝙃𝘼🕊️⃝🦋⁪⁬𝙈𝙐𝙎𝙄𝘾[{BOT_NAME}](https://t.me/QueenAlishaRobot{BOT_USERNAME})✪✪✪

➮ **𝐀𝐥𝐢𝐬𝐡𝐚 𝐒𝐞𝐫𝐯𝐞𝐫 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐅𝐢𝐧𝐞😇**

➮ **ᴢᴀɪᴅ ᴠᴇʀꜱɪᴏɴ : 9.0 Lҽƚҽʂƚ**

➮ **ᴍʏ ᴏᴡɴᴇʀ : [{OWNER_NAME}](https://t.me/Venom_Hai_Hum{अभिमन्यु सिंह राणा})**

➮ **ꜱᴇʀᴠɪᴄᴇ ᴜᴘᴛɪᴍᴇ : `{uptime}`**

**𝚃𝚑𝚊𝚗𝚔𝚜 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝚣𝚊𝚒𝚍 𝙱𝚘𝚝𝚜 ♥️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫 ɢʀᴏᴜᴘ", url=f"https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "ᴄʜᴀɴɴᴇʟ ☑️", url=f"https://t.me/ABOUTABHI"
                    )
                ]
            ]
        )
    )

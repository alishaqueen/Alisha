#zaid Project 
#Ur Motherfucker If U Kang And Don't Give Creadits ๐ฅด

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
        caption=f"""โชโชโช สษชษช ษช แด ไน๐ผ๐๐๐๐๐ผ๐๏ธโ๐ฆโชโฌ๐๐๐๐๐พ[{BOT_NAME}](https://t.me/QueenAlishaRobot{BOT_USERNAME})โชโชโช

โฎ **๐๐ฅ๐ข๐ฌ๐ก๐ ๐๐๐ซ๐ฏ๐๐ซ ๐๐จ๐ซ๐ค๐ข๐ง๐  ๐๐ข๐ง๐๐**

โฎ **แดขแดษชแด แด แดส๊ฑษชแดษด : 9.0 Lาฝฦาฝสฦ**

โฎ **แดส แดแดกษดแดส : [{OWNER_NAME}](https://t.me/Venom_Hai_Hum{เคเคญเคฟเคฎเคจเฅเคฏเฅ เคธเคฟเคเคน เคฐเคพเคฃเคพ})**

โฎ **๊ฑแดสแด ษชแดแด แดแดแดษชแดแด : `{uptime}`**

**๐๐๐๐๐๐ ๐ต๐๐ ๐๐๐๐๐ ๐ฃ๐๐๐ ๐ฑ๐๐๐ โฅ๏ธ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ซ ษขสแดแดแด", url=f"https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "แดสแดษดษดแดส โ๏ธ", url=f"https://t.me/ABOUTABHI"
                    )
                ]
            ]
        )
    )

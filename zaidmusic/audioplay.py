# this module i created only for playing music using audio file, idk, because the audio player on play.py module not working
# so this is the alternative
# audio play function
#Ur motherfucker If U Kang And Don't Give Creadits

from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT, UPDATES_CHANNEL, AUD_IMG, QUE_IMG, GROUP_SUPPORT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("stream") & other_filters)
@errors
async def stream(_, message: Message):

    lel = await message.reply("๐ **๐๐ซ๐จ๐๐๐ฌ๐ฌ๐ข๐ง๐ ** ๐๐ฅ๐ข๐ฌ๐ก๐ ๐๐ฅ๐๐ฒ๐๐ซ...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ษขสแดแดแด",
                        url=f"https://t.me/Shayri_Music_Lovers"),
                    InlineKeyboardButton(
                        text="แดสแดษดษดแดส",
                        url=f"https://t.me/ABOUTABHI")
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"โ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("ษขษชแด แด ๊ฑแดแดแดแดสษชษดษข๊ฑ สษชแดแด แดแดแดษชแด ๊ฐษชสแด๊ฑ แดษดแด สแด สษชษดแด!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{QUE_IMG}",
        reply_markup=keyboard,
        caption=f"#โฃ  สแดแดส สแดQแดแด๊ฑแดแดแด ๊ฑแดษดษข ษชษด **Qแดแดแดแด** แดแด แดแด๊ฑษชแดษชแดษด {position} !\n\nโก __๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ {bn} ๐๐ฅ๐ข๐ฌ๐ก๐__")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUD_IMG}",
        reply_markup=keyboard,
        caption=f"๐ก **ษดแดแดก แดสแดสษชษดษข** แด ๊ฑแดษดษข สแดQแดแดแดแดแด สส {costumer} !\n\nโก __๐๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ {bn} ๐๐ฅ๐ข๐ฌ๐ก๐__"
        )
        return await lel.delete()

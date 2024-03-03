
from pyrogram import filters
from pyrogram.types import Message

from BgtxD.config import BANNED_USERS
from BgtxD.power import get_command
from BgtxD import app
from BgtxD.centre.call import BIKASH
from BgtxD.utility.database import is_music_playing, music_off
from BgtxD.utility.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await BIKASH.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention)
    )

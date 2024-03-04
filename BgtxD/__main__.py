# BGT-MUSIC

import sys
import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from BgtxD import config 
from BgtxD.config import BANNED_USERS
from BgtxD import LOGGER, app, userbot
from BgtxD.centre.call import BIKASH
from BgtxD.modules import ALL_MODULES
from BgtxD.utility.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop_policy().get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("BgtxD").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("BgtxD").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BgtxD.modules" + all_module)
    LOGGER("BgtxD.modules").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await BIKASH.decorators()
    LOGGER("BgtxD").info("BGT Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("BgtxD").info("Stopping BGT Music Bot! GoodBye")

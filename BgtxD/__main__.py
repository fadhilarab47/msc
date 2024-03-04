import asyncio
import importlib

from pyrogram import idle
from BgtxD import config
from BgtxD import LOGGER, app, userbot
from BgtxD.centre.call import BIKASH
from BgtxD.misc import sudo
from BgtxD.modules import ALL_MODULES
from BgtxD.utility.database import get_banned_users, get_gbanned
from BgtxD.config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
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
    LOGGER("BgtxD.modules").info("Successfully Imported Modules...")
    await userbot.start()
    await BIKASH.start()
    await BIKASH.decorators()
    LOGGER("BgtxD").info(
        "BGT Started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("BgtxD").info("Stopping BGT Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

from BgtxD.centre.bot import BIKASH
from BgtxD.centre.dir import dirr
from BgtxD.centre.git import git
from BgtxD.centre.userbot import Userbot
from BgtxD.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = BIKASH()
userbot = Userbot()


from .player import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

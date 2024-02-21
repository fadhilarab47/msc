from BgtxD.core.bot import BgtxD
from BgtxD.core.dir import dirr
from BgtxD.core.git import git
from BgtxD.core.userbot import Userbot
from BgtxD.misc import dbb, heroku, sudo
from BgtxD.platforms import *
from BgtxD.logging import LOGGER

dirr()
git()
dbb()
heroku()
sudo()
app = BgtxD()
userbot = Userbot()
YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

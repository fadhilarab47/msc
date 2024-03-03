# BGT-MUSIC

from BgtxD.centre.bot import BGT
from BgtxD.centre.git import git
from BgtxD.centre.dir import dirr
from BgtxD.logging import LOGGER
from BgtxD.centre.userbot import Userbot
from BgtxD.misc import dbb, heroku, sudo

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = BGT()

# Assistant Client
userbot = Userbot()

from .player import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

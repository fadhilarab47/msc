# BGT-MUSIC

from BgtxD.core.bot import BGT
from BgtxD.core.git import git
from BgtxD.core.dir import dirr
from BgtxD.logging import LOGGER
from BgtxD.core.userbot import Userbot
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

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

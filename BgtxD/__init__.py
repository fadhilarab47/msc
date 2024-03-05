from BgtxD.centre.bot import BGT
from BgtxD.centre.dir import dirr
from BgtxD.centre.git import git
from BgtxD.centre.userbot import Userbot
from BgtxD.misc import dbb, heroku, sudo

from .logging import LOGGER

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

### ----------
app = BGT()

### ----------
userbot = Userbot()


from .player import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

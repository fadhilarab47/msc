import os
import re
import textwrap
import numpy as np
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch

from BgtxD.config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def circle(img):
    h, w = img.size
    a = Image.new('L', [h, w], 0)
    b = ImageDraw.Draw(a)
    
    # Draw outer pie slice
    b.pieslice([(0, 0), (h, w)], 0, 360, fill=255, outline="white")
    
    # Draw inner pie slice to create border effect
    b.pieslice([(70, 70), (h - 70, w - 70)], 0, 360, fill=0, outline="white")
    
    c = np.array(img)
    d = np.array(a)
    e = np.dstack((c, d))
    return Image.fromarray(e)



async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"cache/thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        zyoutube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        logo = circle(zyoutube).resize((474, 474))
        background.paste(logo, (50, 100), mask=logo)  # Adjusted placement of YouTube circle image
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("BgtxD/power/font2.ttf", 40)
        font2 = ImageFont.truetype("BgtxD/power/font2.ttf", 70)
        arial = ImageFont.truetype("BgtxD/power/font2.ttf", 30)
        name_font = ImageFont.truetype("BgtxD/power/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (5, 5), f"{MUSIC_BOT_NAME}", fill="white", stroke_fill="yellow", font=name_font, stroke_width=1
        )
        draw.text(
            (600, 150),
            "BGT-PLAYER",
            fill="white",
            stroke_width=2,
            stroke_fill="yellow",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="yellow",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="yellow",
                    font=font,
                )

        draw.text(
            (600, 450),
            f"Views : {views[:23]}",
            (255, 255, 255),
            font=font,
        )
        draw.text(
            (600, 500),
            f"Duration : {duration[:23]} Mins",
            (255, 255, 255),
            font=font,
        )
        draw.text(
            (600, 550),
            f"Channel : {channel}",
            (255, 255, 255),
            font=font,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png")
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL

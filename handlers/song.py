# Telegramda yani ben boş işler müdürü :) <> Tarafından düzenlenen ufak çaplı proje. 
import os
import requests
import aiohttp
import yt_dlp
import wget

from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME
from helpers.filters import command


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


@Client.on_message(command(["bul"]))
def bul(client, message):

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = "".join(" " + str(i) for i in message.command[1:])
    print(query)
    m = message.reply("🔎 **𝐀𝐫𝐢𝐲𝐨𝐫𝐮𝐦 . . .**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=5).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "• **𝐇𝐢𝐜 𝐁𝐢𝐫 𝐒𝐞𝐲 𝐁𝐮𝐥𝐮𝐧𝐚𝐦𝐚𝐝𝐢 !**\n\n• **𝐁𝐚𝐬𝐤𝐚 𝐁𝐢𝐫 𝐒𝐚𝐫𝐤𝐢 𝐀𝐝𝐢 𝐕𝐞𝐫𝐢𝐧 !**"
        )
        print(str(e))
        return
    m.edit("• **𝐒𝐚𝐫𝐤𝐢 𝐈𝐧𝐝𝐢𝐫𝐢𝐥𝐢𝐲𝐨𝐫 . . .** \n• **𝐋𝐮𝐭𝐟𝐞𝐧 𝐁𝐞𝐤𝐥𝐞𝐲𝐢𝐧 . . .**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"📝 **𝐈𝐬𝐦𝐢**: [{title[:35]}]({link})\n📩 **𝐊𝐚𝐲𝐧𝐚𝐤**: 𝐘𝐨𝐮𝐓𝐮𝐛𝐞\n⌚ **𝐒𝐮𝐫𝐞**: `{duration}`\n👁‍🗨 **𝐆𝐨𝐫𝐮𝐧𝐭𝐮𝐥𝐞𝐦𝐞**: `{views}`\n📔 **𝐓𝐚𝐫𝐚𝐟𝐢𝐧𝐝𝐚𝐧**: **Music**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("❌ 𝐇𝐀𝐓𝐀")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@Client.on_message(
    command(["vbul"]) & ~filters.edited
)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("• **𝐕𝐈𝐃𝐄𝐎 𝐈𝐍𝐃𝐈𝐑𝐈𝐋𝐈𝐘𝐎𝐑 ...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **𝐇𝐀𝐓𝐀:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("• **𝐕𝐈𝐃𝐄𝐎 𝐘𝐔𝐊𝐋𝐄𝐍𝐈𝐘𝐎𝐑 ...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)

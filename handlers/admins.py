from asyncio.queues import QueueEmpty
from cache.admins import admins
from asyncio import sleep
from pyrogram import Client
from pyrogram.types import Message
from callsmusic import callsmusic
from pyrogram import filters

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []

@Client.on_message(command(["durdur"]) & other_filters)
@errors
@authorized_users_only
async def durdur(_, message: Message):
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    a = await message.reply_text("ā¶ļø **šš®š³š¢š¤ šš®š«šš®š«š®š„šš® !**\n\nā¢ **ššš„š¦šš²š šššÆšš¦ šš­š¦šš¤ š¢šš¢š§\n /devam ššØš¦š®š­š®š§š® šš®š„š„šš§š¢š§ !**")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["devam"]) & other_filters)
@errors
@authorized_users_only
async def devam(_, message: Message):
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    a = await message.reply_text("āø **šš®š³š¢š¤ šššÆšš¦ ššš¢š²šØš« !**\n\nā¢ **šš®š«šš®š«š¦šš¤ š¢šš¢š§ /durdur ššØš¦š®š­š®š§š® šš®š„š„šš§š¢š§ !**")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["son"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = message.chat.id 
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("ā¢ **šš® šš§šš šš®š³š¢š¤ ššš„š¦š¢š²šØš« !**")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await callsmusic.pytgcalls.leave_group_call(chat_id)
        await _.send_message(
            message.chat.id,
            "ā **šš®š³š¢š¤ ššØš§š„šš§šš¢š«š¢š„šš¢ !**\n\nā¢ **ššš¬š„š¢ ššØš”ššš­š­šš§ šš²š«š¢š„š¢š²šØš«š®š¦ !**"
        )
    
@Client.on_message(command(["atla"]) & other_filters)
@errors
@authorized_users_only
async def atla(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        a = await message.reply_text("ā¢ **ššš¬š„š¢ ššØš”ššš­š­š šš®š³š¢š¤ ššØš¤ !**")
        await sleep(3)
        await a.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
            
        a = await message.reply_text("ā”ļø **ššš«š¤š¢ šš­š„šš­š¢š„šš¢ . . .**")
        await sleep(3)
        await a.delete()

# Yetki Vermek iĆ§in (ver) Yetki almak iĆ§in (al) komutlarÄ±nÄ± ekledim.
# Gayet gĆ¼zel Ć§alÄ±ÅÄ±yor. @Mahoaga TarafÄ±ndan EklenmiÅtir. 
@Client.on_message(command("ver") & other_filters)
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("KullanÄ±cÄ±ya Yetki Vermek iĆ§in yanÄ±tlayÄ±nÄ±z!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanÄ±cÄ± yetkili.")
    else:
        await message.reply("ā KullanÄ±cÄ± Zaten Yetkili!")


@Client.on_message(command("al") & other_filters)
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("ā KullanÄ±cÄ±yÄ± yetkisizleÅtirmek iĆ§in mesaj atÄ±nÄ±z!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanÄ±cÄ± yetkisiz")
    else:
        await message.reply("ā KullanÄ±cÄ±nÄ±n yetkisi alÄ±ndÄ±!")


# Sesli sohbet iĆ§in 0-200 arasÄ± yeni komut eklenmiÅ oldu. 
@Client.on_message(command(["ses"]) & other_filters)
@authorized_users_only
async def change_ses(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       callsmusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"ā **Birim olarak ayarlandÄ±:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**hata:** {e}")

@Client.on_message(command("reload") & other_filters)
@errors
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await client.send_message(
        message.chat.id,
        "ā **ššØš­ ššš§š¢ššš§ ššš¬š„šš­š¢š„šš¢ !**\nā **ššš¦š¢š§ šš¢š¬š­šš¬š¢ šš®š§ššš„š„šš§šš¢ !**"
    )

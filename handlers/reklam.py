import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as aditya
from config import SUDO_USERS

@Client.on_message(filters.command(["reklam"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**𝐑𝐞𝐤𝐥𝐚𝐦 𝐘𝐚𝐲𝐢𝐧𝐢 𝐁𝐚𝐬𝐥𝐢𝐲𝐨𝐫 ...**")
        if not message.reply_to_message:
            await wtf.edit("**𝐋𝐮𝐭𝐟𝐞𝐧 𝐁𝐞𝐤𝐥𝐞𝐲𝐢𝐧 ...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**𝐑𝐞𝐤𝐥𝐚𝐦 𝐁𝐚𝐬𝐚𝐫𝐢𝐲𝐥𝐚 𝐈𝐥𝐞𝐭𝐢𝐥𝐝𝐢** \n\n**𝐆𝐨𝐧𝐝𝐞𝐫𝐢𝐥𝐝𝐢𝐠𝐢 𝐒𝐨𝐡𝐛𝐞𝐭𝐥𝐞𝐫:** `{sent}` \n**𝐁𝐚𝐬𝐚𝐫𝐢𝐬𝐢𝐳 𝐒𝐨𝐡𝐛𝐞𝐭𝐥𝐞𝐫:** {failed} ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"**𝐑𝐞𝐤𝐥𝐚𝐦 𝐁𝐚𝐬𝐚𝐫𝐢𝐲𝐥𝐚 𝐈𝐥𝐞𝐭𝐢𝐥𝐝𝐢** \n\n**𝐆𝐨𝐧𝐝𝐞𝐫𝐢𝐥𝐝𝐢𝐠𝐢 𝐒𝐨𝐡𝐛𝐞𝐭𝐥𝐞𝐫:** `{sent}` \n**𝐁𝐚𝐬𝐚𝐫𝐢𝐬𝐢𝐳 𝐒𝐨𝐡𝐛𝐞𝐭𝐥𝐞𝐫:** {failed} ")

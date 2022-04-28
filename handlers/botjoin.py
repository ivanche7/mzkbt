from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["katil"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>**𝐁𝐞𝐧𝐢 𝐎𝐧𝐜𝐞 𝐘𝐨𝐧𝐞𝐭𝐢𝐜𝐢 𝐘𝐚𝐩𝐦𝐚𝐥𝐢𝐬𝐢𝐧 .**</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Sesmusic Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"**𝐒𝐞𝐧 𝐠𝐞𝐥 𝐝𝐞𝐫𝐬𝐢𝐧 𝐝𝐞 𝐁𝐞𝐧 𝐠𝐞𝐥𝐦𝐞𝐳 𝐌𝐢𝐲𝐢𝐦 !**")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>**𝐀𝐬𝐢𝐬𝐭𝐚𝐧 𝐆𝐫𝐮𝐛𝐚 𝐊𝐚𝐭𝐢𝐥𝐝𝐢 !**</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔵 𝐇𝐀𝐓𝐀 🔵\n **𝐊𝐮𝐥𝐥𝐚𝐧𝐢𝐜𝐢 {user.first_name} 𝐘𝐨𝐠𝐮𝐧 𝐊𝐮𝐥𝐥𝐚𝐧𝐢𝐦𝐥𝐚𝐫 𝐧𝐞𝐝𝐞𝐧𝐢𝐲𝐥𝐞 𝐆𝐫𝐮𝐛𝐚 𝐊𝐚𝐭𝐢𝐥𝐚𝐦𝐚𝐝𝐢 ! 𝐀𝐬𝐢𝐬𝐭𝐚𝐧𝐢𝐧 𝐲𝐚𝐬𝐚𝐤𝐥𝐢 𝐨𝐥𝐮𝐩 𝐨𝐥𝐦𝐚𝐝𝐢𝐠𝐢𝐧𝐝𝐚𝐧 𝐞𝐦𝐢𝐧 𝐨𝐥𝐮𝐧.**"
            "\n\n **𝐘𝐚𝐝𝐚 𝐀𝐬𝐢𝐬𝐭𝐚𝐧 𝐇𝐞𝐬𝐚𝐛𝐢𝐧𝐢 𝐊𝐞𝐧𝐝𝐢𝐧 𝐄𝐤𝐥𝐞** </b>",
        )
        return
    await message.reply_text(
            "<b>**𝐀𝐬𝐢𝐬𝐭𝐚𝐧 𝐙𝐚𝐭𝐞𝐧 𝐆𝐫𝐮𝐛𝐭𝐚 𝐕𝐚𝐫 !**</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>**𝐀𝐬𝐢𝐬𝐭𝐚𝐧 𝐆𝐫𝐮𝐛𝐭𝐚𝐧 𝐀𝐲𝐫𝐢𝐥𝐚𝐦𝐚𝐝𝐢 !**"
            "\n\n**𝐘𝐚 𝐝𝐚 𝐊𝐞𝐧𝐝𝐢𝐧 𝐂𝐢𝐤𝐚𝐫𝐚𝐛𝐢𝐥𝐢𝐫𝐬𝐢𝐧**</b>",
        )
        return
 
 
 

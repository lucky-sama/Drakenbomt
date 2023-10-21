#(©)Codexbotz

from pyrogram import Client, filters, __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_message(filters.command('about') & filters.private)
async def start_command(client: Client, message: Message):
    await message.reply_photo(
            photo="https://graph.org/file/648bb4dba065accd53c5c.jpg",
            caption="""<b>ᴍʏ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b>

<b>╭━━━━━━━━━━━━━━━━━━━━━</b>
┃
┣⪼<b>Bᴏᴛ Nᴀᴍᴇ : <a href='https://t.me/Arsenal_Bots_Updates'>File Sharing Bot</a>
┣⪼<b>Dᴇᴠᴇʟᴏᴩᴇʀ: <a href='https://t.me/Shadow_XD_ChatBot'>ꕶʜᴀᴅᴏꪝ</a>
┣⪼<b>Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ</b>
┣⪼<b>Bᴇꜱᴛ Fʀɪᴇɴᴅ: <a href='tg://settings'>Tʜɪꜱ Pᴇʀꜱᴏɴ</a>
┣⪼<b>Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3</b>
┣⪼<b>Oᴜʀ Cᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Team_XDs'>Xᴛʀᴀ Dᴇsᴄᴇɴᴛs</a>
┃
<b>╰━━━━━━━━━━━━━━━</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Dᴇᴠ/Oᴡɴᴇʀ", url="https://t.me/Shadow_XD_ChatBot")],
                ]
            ),
            
        )

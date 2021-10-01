from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import BOT_USERNAME

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"💕Hҽɾҽ Aʂʂιʂƚαɳƚ Oϝ @{BOT_USERNAME}\n✨This Bσƚ Dҽρʅσყ Bყ @XD_LIF [𝕵𝖆𝖓𝖛𝖎](https://t.me/HEENAXD)\n🌟𝗗𝗼𝗻𝘁 𝗦𝗽𝗮𝗺 𝗛𝗲𝗿𝗲")
  return                        

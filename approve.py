# MIT License

# Copyright (c) 2022 Muhammed

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Telegram Link : https://telegram.dog/Mo_Tech_Group
# Repo Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot
# License Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot/blob/Auto-Approved-Bot/LICENSE

from os import environ
from pyrogram import Client, filters, enums, errors
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "Auto Approved Bot",
    bot_token = environ["BOT_TOKEN"],
    api_id = int(environ["API_ID"]),
    api_hash = environ["API_HASH"]
)

CHAT_ID = [int(pr0fess0r_99) for pr0fess0r_99 in environ.get("CHAT_ID", None).split()]
#TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
TEXT = """<b>Hello {mention},

<blockquote>Yᴏᴜʀ Rᴇqᴜᴇꜱᴛ Tᴏ Jᴏɪɴ {title} Hᴀꜱ Bᴇᴇɴ Aᴩᴩʀᴏᴠᴇᴅ 🔥</blockquote>

Send /start to know more.</b>"""

APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    #approvedbot = await client.get_me() 
    button = [[
                InlineKeyboardButton('♻️ GROUP', url='https://t.me/MovieJunctionGrp'),
                InlineKeyboardButton('CHANNELS 🏷️', url='https://t.me/Mj_Linkz/1318')
         ]]
    await client.send_message(chat_id=message.chat.id, text=f"<b>Hᴇʟʟᴏ {message.from_user.mention}!\n\n<blockquote>🤖 I'ᴀᴍ Aɴ Aᴜᴛᴏ Aᴩᴩʀᴏᴠᴀʟ Bᴏᴛ 💥</blockquote></b>\n\n⚠️ 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 & 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝘁𝗼 𝗞𝗻𝗼𝘄 𝗠𝗼𝗿𝗲 👇", reply_markup=InlineKeyboardMarkup(button), parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    try:       
         await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
         print(f"{user.first_name} Joined {chat.title} 🤝") # Logs
         ##if APPROVED == "on":
         buttons = [[
                InlineKeyboardButton('♻️ GROUP', url='https://t.me/MovieJunctionGrp'),
                InlineKeyboardButton('CHANNELS 🏷️', url='https://t.me/Mj_Linkz/1318')
         ]]
         reply_markup = InlineKeyboardMarkup(buttons)    
         await client.send_message(chat_id=user.id, text=TEXT.format(mention=user.mention, title=chat.title), reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.HTML, disable_web_page_preview=True)
    except errors.PeerIdInvalid as e:
         print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    

print("Auto Approved Bot")
pr0fess0r_99.run()

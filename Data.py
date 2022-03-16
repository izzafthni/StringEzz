from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
hai {}

Selamat datang di {}

Jika anda tidak mempercayai bot ini, 
1) Stop membaca tulisan ini
2) Hapus obrolan dan blokir bot ini

Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

By @StringEzz
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton("Bot Status and More Bots", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use?", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
      
        
    )

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @StringEzz

Source Code : [Click Here](https://github.com/izzafthni/StringEzz)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """ 

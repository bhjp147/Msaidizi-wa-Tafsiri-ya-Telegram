import os
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from googletrans import Translator
TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", 12345))

API_HASH = os.environ.get("API_HASH", "")
app = Client(
        "Gtt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=API_ID
    )

@app.on_message(filters.private & filters.command(['start']))
async def start(client, message):
	await message.reply_text(text =f"Hello **{message.from_user.first_name }** \n\n __I am simple Google Translater Bot \n I can translate any language to you selected language__",reply_to_message_id = message.message_id ,parse_mode="markdown", reply_markup=InlineKeyboardMarkup([ [                    InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/lntechnical") ],               [InlineKeyboardButton("Subscribe 🧐", url="https://youtube.com/c/LNtechnical") ]   ]  ) )
                  



@app.on_message(filters.private & filters.text  )
async def echo(client, message):

 
 keybord1= InlineKeyboardMarkup( [
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Next --->",callback_data = "page2")
	]
	] )
	
 await  message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord1) 


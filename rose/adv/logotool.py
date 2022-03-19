from rose import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup, InputMediaPhoto
import os
from requests import get
import requests
from PIL import Image
import io

logo = """
**How to Use Logo Creator Tool**

× /logo `[TEXT]`: Create a logo 

**Available Features**
- 5000+ Fonts Available .
- 10000+ Background Images.
- Never Expire Image Links. [Telegraph](https://telegra.ph/file/8b7b44d8c000c89a16f8f.jpg)
- Group / Channel & Inbox Supported.

Original work is done by [@Call_me_futurepilot](https://telegra.ph/file/529c5b49f4e40baeca030.jpg) | [Our Channel </>](https://t.me/mahsoombotupdate)
"""
ghost = """
**How to Use Logo Creator Tool**

× /slogo `[TEXT]` : New Beautiful trending logo

**Available Features**
- Ghostist Logo [API](https://telegra.ph/file/8b7b44d8c000c89a16f8f.jpg)

Original work is done by [@Call_me_futurepilot](https://telegra.ph/file/529c5b49f4e40baeca030.jpg) | [Our Channel </>](https://t.me/mahsoombotupdate)
"""
hql = """
× /logohq `[TEXT]`: Create a HQ logo 
**How to Use Logo Creator Tool**


× /logohq `[TEXT]`: Create a HQ logo 

**Available Features**
- 5000+ Fonts Available .
- 10000+ Background Images.
- Quick Response. [API Base](https://telegra.ph/file/10a82d98ba84bf7220563.jpg)
- Never Expire Image Links. [Telegraph](https://telegra.ph/file/8b7b44d8c000c89a16f8f.jpg)
- 4K Logo & Wallpapers.
- Group / Channel & Inbox Supported.


Original work is done by [@Call_me_futurepilot](https://telegra.ph/file/529c5b49f4e40baeca030.jpg) | [Our Channel </>](https://t.me/mahsoombotupdate)
"""
hand = """

**How to Use Logo Creator Tool**


× /write `[TEXT]` : hand writer

**Available Features**
- Group / Channel & Inbox Supported.
- Hand Writing [sinhala & English ](https://t.me/mahsoombotupdate)


Original work is done by [@Call_me_futurepilot](https://telegra.ph/file/529c5b49f4e40baeca030.jpg) | [Our Channel </>](https://t.me/mahsoombotupdate)
"""
wall = """
**How to Use Logo Creator Tool**


×  /wall `[TEXT]` : search wallpapers

**Available Features**
- 5000+ Fonts Available .
- 10000+ Background Images.
- Quick Response. [API Base](https://t.me/mahsoombotupdate)
- Never Expire Image Links. [Telegraph](https://telegra.ph/file/8b7b44d8c000c89a16f8f.jpg)
- 4K Logo & Wallpapers.
- Group / Channel & Inbox Supported.


Original work is done by [@Call_me_futurepilot](https://telegra.ph/file/529c5b49f4e40baeca030.jpg) | [Our Channel </>](https://t.me/mahsoombotupdate)
"""

@app.on_callback_query(filters.regex("pic"))
async def mylogo(_, query):
    text = query.from_user.first_name
    mode = query.data.split()[1].strip()
    if mode == "logo" or not query.from_user.photo:
        await query.answer("⚙️ Creating Your ghost..", show_alert=True)
        LOGO_API = f"https://api.single-developers.software/logo?name={text}"
        randc = (LOGO_API)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        murl = requests.get(f"https://api.single-developers.software/logo?name={text}").history[1].url
        await query.edit_message_media(InputMediaPhoto(media=murl, caption=logo), reply_markup=asuttons)
    if mode == "ghost" or not query.from_user.photo:
        await query.answer("⚙️ Creating Your ghost..", show_alert=True)
        req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={text}")
        IMG = req.text
        await query.edit_message_media(InputMediaPhoto(media=IMG, caption=ghost), reply_markup=asuttons)
    if mode == "hql" or not query.from_user.photo:
        await query.answer("⚙️ Creating Your HQ..", show_alert=True)
        q = "none"
        photo = get(f"https://api.single-developers.software/logohq?name={text}").history[1].url
        await query.edit_message_media(InputMediaPhoto(media=photo, caption=hql), reply_markup=asuttons)
    if mode == "hand" or not query.from_user.photo:
        await query.answer(" ⚙️ Creating Your Hand-Write..", show_alert=True)
        API = "https://api.single-developers.software/write"
        body = {     
     "text":f"""
Hello ! {text} Hijab Queen is one of the fastest and most feature filled group manager.

Why Hijab Queen:
- Simple: Easy usage and compaitble with many bot commands.
- Featured: Many features which other group management bots don't have.
- Fast: Pyrogram base bot and use mongo as database.

"""    
           }
        req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)
        img = req.history[1].url
        await query.edit_message_media(InputMediaPhoto(media=img, caption=hand), reply_markup=asuttons)
    if mode == "wall" or not query.from_user.photo:
        await query.answer("⚙️ Creating Your Wallpaper...", show_alert=True)
        q = "none"
        photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
        await query.edit_message_media(InputMediaPhoto(media=photo, caption=wall), reply_markup=asuttons)
 




asuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton
                (
                    "Logo-tool", callback_data="pic logo"
                ),            
            InlineKeyboardButton
                (
                    "Ghostist-logo", callback_data="pic ghost"
                ) 
        ],
        [
            InlineKeyboardButton
                (
                    "HQ-logo", callback_data="pic hql"
                ),            
            InlineKeyboardButton
                (
                    "Hand-Write", callback_data="pic hand"
                )  
        ], 
        [
            InlineKeyboardButton
                (
                    "Wallpapers", callback_data="pic wall"
                )
        ],      
        [
            InlineKeyboardButton
                (
                    "🔙Back", callback_data="adv_menu"
                )
        ]
    ]
)

upun = """
**How to Use Logo Creator Tool**

**Available Features**

- 5000+ Fonts Available .
- 10000+ Background Images.
- Quick Response. [API Base](https://t.me/mahsoombotupdate)
- Never Expire Image Links. [Telegraph](https://telegra.ph/file/8b7b44d8c000c89a16f8f.jpg)
- 4K Logo & Wallpapers.
- Group / Channel & Inbox Supported.
- Hand Writing [sinhala & English ](https://t.me/mahsoombotupdate)
- Ghostist Logo [API](https://telegra.ph/file/8b7b44d8c000c89a16f8f.jpg)

**Original work is done by **[@Call_me_futurepilot](https://telegra.ph/file/529c5b49f4e40baeca030.jpg) | [Our Channel </>](https://t.me/mahsoombotupdate)
"""
photo = "https://telegra.ph/file/529c5b49f4e40baeca030.jpg"

@app.on_callback_query(filters.regex("_logo"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_photo(
        CallbackQuery.message.chat.id,
        photo = photo,
        caption=upun,
        reply_markup=asuttons,
    )
    await CallbackQuery.message.delete()
 

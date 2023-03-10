from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



START_MESSAGE = '''**{},
I am Omega Links Converter Bot. I Can Convert Links Directly From Your OmegaLinks.in Account,
    
Go To** π https://omegalinks.in/member/tools/api?connect=true
**π€ Than Hit Start If You're Redirected To Bot.**

Other Ways π

1. **Go To** π https://omegalinks.in/member/tools/api
2. **Than Copy** API Key
3. **Than Type** `/api` than give a single space and than paste your API Key
**(see example to understand more...)**

/api <space> API Key 
(See Example.π)
**Example:**
 `/api 9c5a6c96077a1b499d8f953331221159383eb434 `

**π€ Hit** π /features To Know More Features Of This Bot.
**πββοΈ Hit** π /help To Get Help.
**β Hit** π /channel To Get Help About Adding your channel to bot.
**β Hit** π /footer To Get Help About Adding your Custom Footer to bot.

If You are new to OmegaLinks then click on below button to create your account.'''

HELP_MESSAGE = '''**{},**

Ιͺ  α΄α΄Ι΄  α΄α΄Ι΄α΄ α΄Κα΄  α΄Ι΄Κ  α΄ΙͺΚα΄α΄α΄  ΚΙͺΙ΄α΄  ΙͺΙ΄α΄α΄  Κα΄α΄Κ  α΄ΚΚ  κ±Κα΄Κα΄α΄ΚΙ΄  ΚΙͺΙ΄α΄κ±.
    
π.  Ι’α΄  α΄α΄  π  https://omegalinks.in/member/tools/api
  
π.  α΄Κα΄Ι΄  α΄α΄α΄Κ  **α΄α΄Ιͺ  α΄α΄Κ**

π.  α΄Κα΄Ι΄  α΄Κα΄α΄  **/api  Κα΄α΄Κ  α΄α΄Ιͺ  α΄α΄Κ**


π£οΈ   ππ±ππ¦π©π₯π:

`/api 9c5a6c96077a1b499d8f953331221159383eb434 `


π£οΈ  /features  α΄α΄  α΄Ι΄α΄α΄‘  α΄α΄Κα΄  κ°α΄α΄α΄α΄Κα΄κ±  α΄κ°  α΄ΚΙͺκ±  Κα΄α΄.

ππππ :  κ°α΄Κ  α΄α΄α΄α΄ΙͺΚκ± π π'''

ABOUT_TEXT = '''**
I am Omega Links Converter Bot. I Can Convert Links Directly From Your OmegaLinks.in Account,**

**β‘Featuresβ‘**

**β’ I can Convert any links or posts to your OmegaLinks link / post. (Button Links Posts, Hidden links/Hyperlinks All Are Supported)**

**β’ I can Convert unlimited OmegaLinks.in links at once.** (if you are sending a list of urls.)

**β’ No need to share password or email to convert links.**

**β’ I Can auto add custom footer text to your every post. Hit π /footer To know more...**

**β’ I Can auto add custom Header text to your every post. Hit π /Header To know more...**

**β’ I Can replace / remove other's channel links with your channel link. Hit π /channel To know More...**

**β’ I Can Automatically Replace Your Banner Image To images in the post. Hit  π/Banner_image To Know More...**

 Anyone who want to use any **other shortner** instead of OmegaLinks than **contact to owner** (all **shortners support** available.)'''

CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://telegram.me/MovieVillaSupport | Movie Villa"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""

ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('α΄α΄Ι΄α΄α΄α΄α΄  α΄π  πΎα΄‘Ι΄α΄Κ  β£οΈ', url='https://telegram.dog/MovieVillaOwner')
        
    ],


])

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('α΄α΄Ι΄α΄α΄α΄α΄  α΄π  πΎα΄‘Ι΄α΄Κ  β£οΈ', url='https://telegram.dog/MovieVillaOwner')
        
    ],


])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('πͺ  Connect  To  OmegaLinks  βοΈ', url=f'https://omegalinks.in/ref/devil')
    ]
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://omegalinks.in/ref/devil)

- Site Link:
 {base_site}

- Current Linked API:
{shortener_api}

- Channel Username: 
@{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: 
{banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/api [api]`
            
Ex: `/api 9c5a6c96077a1b499d8f953331221159383eb434 `

Get API From [{base_site}](https://omegalinks.in/ref/devil)

Current: {base_site} 
API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """**Reply to the Footer Text You Want**

This Text will be added to the **bottom** of every message **caption** or text

For adding **line break** use \n
To Remove Footer Text: `/footer remove`


ππ±ππ¦π©π₯π:

`/footer
βββββββββββββββββ
πββοΈ How To Download π
π https://youtube.com/@movievillayt
βββββββββββββββββ
π₯ ππ¨π’π§ ππ‘ππ§π§ππ₯ π₯
π https://telegram.dog/Movievillayt`
"""

USERNAME_TEXT = """**α΄Κα΄α΄κ±α΄  α΄Κα΄α΄  ΙͺΙ΄  Ι’Ιͺα΄ α΄Ι΄  κ°α΄Κα΄α΄α΄

/channel (channel link or username)


ππ±ππ¦π©π₯π:

/channel @MovieVillaYT

ππ«

`/channel https://telegram.dog/MovieVillaChat`


π /features  α΄α΄  α΄Ι΄α΄α΄‘  α΄α΄Κα΄  κ°α΄α΄α΄α΄Κα΄κ±  α΄κ°  α΄ΚΙͺκ±  Κα΄α΄."""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://telegra.ph/file/5e96340a91470256b387a.jpg`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""

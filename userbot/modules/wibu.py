# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.wibu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Sial Ada Wibu**")
    sleep(1)
    await typew.edit("**Sekuat Apapun Aku**")
    sleep(1)
    await typew.edit("**Jika Ada Wibu**")
    sleep(1)
    await typew.edit("**Aku Harus Lari**")
    sleep(1)
    await typew.edit("**Lari Cukkk Ada Wibuuu**")
    sleep(1)
    await typew.edit("**Argghhhhhhhhhh**")
    sleep(1)
    await typew.edit("**Lari Sekencang-Kencangnya**")
    sleep(1)
    await typew.edit("**Karena Kita Sedang**")
    sleep(1)
    await typew.edit("**Menghadapi Ras Terkuat**")
    sleep(1)
    await typew.edit("**Yang Ada Di Dunia**")
    sleep(1)
    await typew.edit("**Wibuuuu**")
    sleep(1)
    await typew.edit("**Arghhhhhhhh**")
    sleep(1)
    await typew.edit("**Istrinya Kartun**")
    sleep(1)
    await typew.edit("**Dasar Wibu**")


CMD_HELP.update(
    {
        "king": "**✘ Plugin :** `wibu`\
        \n\n  •  **Perintah :** `.wibu`\
        \n  •  **Function : **Untuk melihat sesuatu yang menarik\
        \n  •  **Function : **Lari Cuk Ada Wibuuu Arghhhh**\
        \n  ** Harap chat developer king @SkyzoSaja Jika ingin mengidekan sesuatu yang menarik **\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @SkyzoSaja Jika ingin mengidekan sesuatu yang menarik **\
    "
    }
)

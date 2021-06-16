# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.eggyol(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.05)
    await typew.edit("**Sial Ada Eggyol Jing😨**")
    sleep(0.05)
    await typew.edit("**Sekuat Apapun Aku😭**")
    sleep(0.05)
    await typew.edit("**Jika Ada Eggyol😨**")
    sleep(0.05)
    await typew.edit("**Aku Harus Lari🏃🏻**")
    sleep(0.05)
    await typew.edit("**Lari Cukkk Ada Eggyol Kwkwkwkwk🏃🏻**")
    sleep(0.05)
    await typew.edit("**Argghh Bangkeee!🏃🏻**")
    sleep(0.05)
    await typew.edit("**Lari Sekencang-Kencangnya🤸🏻**")
    sleep(0.05)
    await typew.edit("**Karena Kita Sedang🤾🏻**")
    sleep(0.05)
    await typew.edit("**Menghadapi🤸🏻**")
    sleep(0.05)
    await typew.edit("**Eggyol Kontol Asu🏃🏻**")
    sleep(0.05)
    await typew.edit("**Aaaaa Eggyol🪂**")
    sleep(0.05)
    await typew.edit("**Arghhhhhhh🧗🏻**")
    sleep(0.05)
    await typew.edit("**Eggyol Sangean🤾🏻**")
    sleep(0.05)
    await typew.edit("**Dasar Eggyol Tolol😨**")
    sleep(0.05)
    await typew.edit("**Maaf Eggyol Kontol🤼‍♂️**")
    sleep(0.05)
    await typew.edit("**Aku Tidak Akan🤾🏻**")
    sleep(0.05)
    await typew.edit("**Mengulanginya Lagi🏃🏻**")
    sleep(0.05)
    await typew.edit("**Tapi Bo'ong🤾🏻**")
    sleep(0.05)
    await typew.edit("**Dasar Eggyol, Sangean🪂**")
    

CMD_HELP.update(
    {
        "king": "**✘ Plugin :** `eggyol`\
        \n\n  •  **Perintah :** `.eggyol`\
        \n  •  **Function : **Untuk melihat sesuatu yang menarik\
        \n  •  **Function : **Lari Cuk Ada Eggyol Asu Arghhhh**\
        \n  ** Harap chat developer king @SkyzoSaja Jika ingin mengidekan sesuatu yang menarik **\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @SkyzoSaja Jika ingin mengidekan sesuatu yang menarik **\
    "
    }
)

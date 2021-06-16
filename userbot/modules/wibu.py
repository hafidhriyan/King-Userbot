# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.wibu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0.05)
    await typew.edit("**Sial Ada Wibu😨**")
    sleep(0.05)
    await typew.edit("**Sekuat Apapun Aku😭**")
    sleep(0.05)
    await typew.edit("**Jika Ada Wibu😨**")
    sleep(0.05)
    await typew.edit("**Aku Harus Lari🏃🏻**")
    sleep(0.05)
    await typew.edit("**Lari Cukkk Ada Wibuuu🏃🏻**")
    sleep(0.05)
    await typew.edit("**Argghh Bangkeee!🏃🏻**")
    sleep(0.05)
    await typew.edit("**Lari Sekencang-Kencangnya🤸🏻**")
    sleep(0.05)
    await typew.edit("**Karena Kita Sedang🤾🏻**")
    sleep(0.05)
    await typew.edit("**Menghadapi Ras Terkuat🤸🏻**")
    sleep(0.05)
    await typew.edit("**Yang Ada Di Dunia🏃🏻**")
    sleep(0.05)
    await typew.edit("**Wibuuuu🪂**")
    sleep(0.05)
    await typew.edit("**Arghhhhhhh🧗🏻**")
    sleep(0.05)
    await typew.edit("**Istrinya Kartun🤾🏻**")
    sleep(0.05)
    await typew.edit("**Dasar Wibu😨**")
    sleep(0.05)
    await typew.edit("**Maaf Wibu🤼‍♂️**")
    sleep(0.05)
    await typew.edit("**Aku Tidak Akan🤾🏻**")
    sleep(0.05)
    await typew.edit("**Mengulanginya Lagi🏃🏻**")
    sleep(0.05)
    await typew.edit("**Tapi Bo'ong🤾🏻**")
    sleep(0.05)
    await typew.edit("**Dasar Wibu, Istri Kartun🪂**")
    

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

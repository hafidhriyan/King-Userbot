# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Pertama-tama kamu cantik**")
    sleep(1)
    await typew.edit("**Kedua kamu manis**")
    sleep(1)
    await typew.edit("**Dan yang terakhir adalah kamu bukan jodohku**")
    sleep(1)
    await typew.edit("**Mengsedih🥺**")
    sleep(1)
    await typew.edit("**Iya Gua Tau Gua Gak**")
    sleep(1)
    await typew.edit("**Goodloking**")
    sleep(1)
    await typew.edit("**Tapi Gua Juga Ada**")
    sleep(1)
    await typew.edit("**Perasaan**")
    sleep(1)
    await typew.edit("**Dan Gua Udah Sayang Ke Elu**")
    sleep(1)
    await typew.edit("**Kok Malah Di Sia-Sia In😭**")
    sleep(1)
    await typew.edit("**Emang Salah Ya Gua Suka Sama Lu?**")
    sleep(1)
    await typew.edit("**Dahlah Males Gua**")
    sleep(1)
    await typew.edit("**Ngentot Lu**")
    sleep(1)
    await typew.edit("😭")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern="^.king(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit(
        " -^-^-^- **S** -^-^-^- \n"
        " -^-^-^- **K** -^-^-^- \n"
        " -^-^-^- **Y** -^-^-^- \n"
        " -^-^-^- **Z** -^-^-^- \n"
        " -^-^-^- **O** -^-^-^- \n"
        "__**🐲USERBOT TELEGRAM🐲**__ \n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"__**Hai aku adalah bot king fork assisten {ALIVE_NAME} yang menjaga akun ini**__ \n"
        "__**Terimakasih**__ \n"
        "**Enjoy Hahaha:)** \n"
        "__**Developer by :**__ [Skyzo](https://t.me/SkyzoSaja) ")


@register(outgoing=True, pattern='^.waebo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ Woi Wibu Nih Gw Kasih`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(-_-)`"
                     "`\n/>💔  Kok Di Patahin Asw`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(°_°)`"
                     "`\n💔<\\  Watashi Minta Maaf:(`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(-_-)`"
                     "`\n/>💔  Yaudah Gapapa, Giniamat Si Wibu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(>_<)`"
                     "`\n🧸<\\  Kyaa Makasih Watashi Suka Kamu >_<`")


CMD_HELP.update(
    {
        "king": "**✘ Plugin :** `king`\
        \n\n  •  **Perintah :** `.king`\
        \n  •  **Function : **Untuk melihat sesuatu yang menarik\
        \n\n  •  **Perintah :** `.sadboy`\
        \n  •  **Function : **Jadi sadboy:)\
        \n\n  •  **Perintah :** `.punten` | `.pantau`\
        \n  •  **Function : **Untuk punten dan pantau\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @SkyzoSaja Jika ingin mengidekan sesuatu yang menarik **\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat developer king @SkyzoSaja Jika ingin mengidekan sesuatu yang menarik **\
    "
    }
)

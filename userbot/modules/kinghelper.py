""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.khelp$")
async def usit(e):
    await e.edit(
        f"      ╔════════════╗\n     ⚡️Skyzo⚡️     \n╚════════════╝ \n"
        f"**Hai King {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "═⎆ Pemilik : [King Apis](t.me/PacarFerdilla) \n"
        "═⎆ Repo    : [Repo](https://github.com/ridho17-ind/King-Userbot) \n"
        "═⎆ Instragam : [Instagram King Flicks](Instagram.com/xyzskyzo) \n"
        "═⎆ Grup Support : [Support](https://t.me/mengvirtual_gc)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"      ╔════════════╗\n  ⚡️𝘿𝘼𝙁𝙏𝘼𝙍 𝙑𝘼𝙍𝙎⚡️     \n╚════════════╝ \n"
        f"**Disini Daftar Vars Dari King {DEFAULTUSER}:**\n"
        "═⎆ Daftar Vars : [DAFTAR VARS](https://raw.githubusercontent.com/apisuserbot/King-Userbot/King-Userbot/varshelper.txt)")


CMD_HELP.update(
    {
        "helper": "**✘ Plugin : **`helper`\
        \n\n  •  **Perintah :** `.khelp`\
        \n  •  **Function : **Bantuan Untuk ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️.\
        \n\n  •  **Perintah :** `.vars`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Perintah :** `.repo`\
        \n  •  **Function : **Melihat Repo ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️.\
        \n\n  •  **Perintah :** `.string`\
        \n  •  **Function : **Link untuk mengambil String ⚡️𝗞𝗶𝗻𝗴-𝙐𝙎𝙀𝙍𝘽𝙊𝙏⚡️.\
    "
    }
)

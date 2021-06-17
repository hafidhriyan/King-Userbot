from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.skyzo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Skyzo`")
    sleep(3)
    await typew.edit("`14 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Jawa, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.beb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.creator(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Skyzo Mastah`")
    sleep(3)
    await typew.edit("`Berlin Manager`")
    sleep(1)
    await typew.edit("`Iky Contributor`")
# Create by myself @localheart

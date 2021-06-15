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

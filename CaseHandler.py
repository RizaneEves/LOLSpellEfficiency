def handleScoreCases(s, score):
    if "SorakaW" in s.getKey():
        return 0
    elif "KarthusDefile" in s.getKey():
        return 0
    return score


def handleCooldownCases(s, cooldown, CDR):
    if "TeemoRCast" in s.getKey():
        return (1 - CDR) * 22.0
    elif "ViE" in s.getKey():
        return (1 - CDR) * 8.0
    elif "XerathArcaneBarrage2" in s.getKey():
        return cooldown + 3.0
    elif "KogMawLivingArtillery" in s.getKey():
        return (1 - CDR) * 6.0

    return cooldown

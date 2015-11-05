"""
This file contains functions that handle certain cases that I believe to be
edge cases that may lead to inaccurate results. Many assumptions are made. Please read README for more info.
Also read comments below.
Please be aware that not all cases are handled, since there are so many things that effect damage and cooldown,
and the Riot API does not provide information on how to handle these.
"""


"""
Handle cases that have to do with the score.
"""
def handleScoreCases(s, score):
    if "SorakaW" in s.getKey():             # Hard wire Soraka's W to a score of 0 since it is perceived to do damage
        return 0                            # even though it doesn't.
    elif "KarthusDefile" in s.getKey():     # Hard wire Karthus's Defile to a score of 0 since although it does massive
        return 0                            # damage per second, it is at a high mana cost and is considered a toggle rather than a spell.
    return score                            # Return the new score

"""
Handle cases that have to do with cooldown
"""
def handleCooldownCases(s, cooldown, CDR):
    if "TeemoRCast" in s.getKey():          # Set Teemo's R to a base cooldown of 22 seconds, since it achieves extremely high
        return (1 - CDR) * 22.0             # efficiency with it's low cooldown of 0.25 seconds, but the recharge time for a mushroom is 22 seconds
    elif "ViE" in s.getKey():               # Set Vi's E to a base cooldown of 8 seconds, because it has a really low cooldown
        return (1 - CDR) * 8.0              # due to it requiring charges, but it takes 8 seconds for her to recharge.
    elif "XerathArcaneBarrage2" in s.getKey():      # Add 3 seconds to Xerath's Arcanopulse, since it
        return cooldown + 3.0                       # takes 3 seconds to charge up completely.
    elif "KogMawLivingArtillery" in s.getKey():     # Hard wire KogMaw's ultimate cooldown to 6 seconds, because repeatedly
        return (1 - CDR) * 6.0                      # it requires massive amounts of mana and is hardly efficient and it resets in 6 seconds.

    return cooldown                                # Return the new cooldown

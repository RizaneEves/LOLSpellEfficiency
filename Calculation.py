from CaseHandler import *
from Spell import *
from Champion import *


def getSpellScore(s, AP, AD, CDR):
    damage = getSpellDamage(s, AP, AD)
    cooldown = getSpellCooldown(s, CDR)
    cost = float((s.getCost())[s.getMaxRank() - 1])

    score = 0
    if "mana" or "energy" in s.getCostType().lower():
        if cost > 0 and cooldown > 0:
            score = damage / cooldown

    score = handleScoreCases(s, score)

    return score


def getSpellDamage(s, AP, AD):
    return spellHasDamage(s) * (getBaseDamage(s) + getVariableDamage(s, AP, AD))


def getBaseDamage(s):
    baseDamage = 0
    if (s.getEffect() is not None):
        if ((s.getEffect())[1] is not None):
            baseDamage = (s.getEffect())[1][s.getMaxRank() - 1]

    return baseDamage


def spellHasDamage(s):
    if s.getVars() is None: return 0
    for var in s.getVars():
        if "damage" in (var["link"]).lower():
            return 1
    return 0


def getVariableDamage(s, AP, AD):
    variableDamage = 0
    if (s.getVars() is None): return 0
    for var in (s.getVars()):
        if ("spelldamage" in (var["link"]).lower()):
            AP_coeff = var["coeff"][0]
            float(AP_coeff)
            variableDamage += (AP * AP_coeff)

        if "attackdamage" in (var["link"]).lower():
            AD_coeff = var["coeff"][0]
            float(AD_coeff)
            variableDamage += (AD * AD_coeff)
    return variableDamage


def getSpellCooldown(s, CDR):
    cooldown = (1 - CDR) * (s.getCooldown())[s.getMaxRank() - 1]
    cooldown = handleCooldownCases(s, cooldown, CDR)
    return cooldown


def getHighestScore(data, AP, AD, CDR):
    highScore = 0
    highChampion = ""
    highSpell = ""
    highSpellDesc = ""

    for key in data["keys"]:
        c = Champion(data, key)
        print(c.getName())

        for s in c.getSpells():
            spell = Spell(s)
            print(spell.getName())
            currScore = getSpellScore(spell, AP, AD, CDR)
            print(str(currScore))
            if currScore > highScore:
                highScore = currScore
                highSpell = spell.getName()
                highChampion = c.getName()
                highSpellDesc = spell.getDescription()
    print(
        "Your results have been calculated based on: " + str(AP) + " AP, " + str(AD) + " AD, " + str(
            CDR * 100) + "% CDR.")
    print("Result: ")
    print("Champion: " + highChampion)
    print("Spell: " + highSpell)
    print("Spell description: " + highSpellDesc)
    print("Reason: This spell has achieved a high score of: " + str(highScore) + ".")

def getSpellScore(s, AP, AD, CDR):

def getSpellDamage(s,AP,AD,CDR):
    return spellHasDamage(s)*(getBaseDamage(s)+ getVariableDamage(s,AP,AD))

def getBaseDamage(s):
    baseDamage = 0
    if(s.getEffect() is not None):
        if((s.getEffect())[1] is not None):
            baseDamage = (s.getEffect())[1][s.getMaxRank()-1]

    return baseDamage

def spellHasDamage(s):
    
    if(s.getVars() is None): return 0
    for(var in s.getVars()):
        if "damage" in (var["link"]).lower():
            return 1
    return 0
        

def getVariableDamage(s,AP,AD):
    variableDamage = 0
    if(s.getVars() is None): return 0
    for(var in s.getVars()):
        if ("spelldamage" in (var["link"]).lower()):
            AP_coeff = var["coeff"][0]
            float(AP_coeff)
            variableDamage += (AP * AP_coeff)

        if "attackdamage" in (var["link"]).lower():
            AD_coeff = var["coeff"][0]
            float(AD_coeff)
            variableDamage += (AD * AD_coeff)
    return variableDamage
    


def getSpellCooldown(s,CDR):
    cooldown = (1-CDR)*s.getCooldown()
    cooldown = handleCooldownCases(s, cooldown)
    return cooldown
from CaseHandler import *
from Spell import *
from Champion import *
"""
This is our Calculation class where all important functions are stored that perform calculations to help us
calculate a spell's efficiency score and thus return the spell with the highest efficiency score.
NOTE: Many assumptions are made in these calculations and they may not be accurate. All of these assumptions are
listed in the readme.
"""

"""
Returns the efficiency score of the spell s based on AP, AD and CDR.
"""
def getSpellScore(s, AP, AD, CDR):
    damage = getSpellDamage(s, AP, AD)                  # Get total spell damage based on AP and AD (at max rank)
    cooldown = getSpellCooldown(s, CDR)                 # Get spell cooldown based on CDR (at max rank)
    cost = float((s.getCost())[s.getMaxRank() - 1])     # Get spell cost at max rank

    score = 0                                           # Initialize the score to 0
    if "mana" or "energy" in s.getCostType().lower():   # If the spell has an Energy or Mana cost, as per my definition of a spell..
        if cost > 0 and cooldown > 0:                   # If the spell has a cost and cooldown greater than zero...
            score = damage / cooldown                   # Calculate my spell efficiency score as  (Total Damage) / Cooldown

    score = handleScoreCases(s, score)                  # Handle certain edge cases based on assumptions made. Read README!

    return score                                        # Return the efficiency score

"""
Return the total damage of the spell s based on AP and AD.
"""
def getSpellDamage(s, AP, AD):
    """
    If the spell has damage, return the total damage which is base damage + scaled variable damage at max rank.
    Otherwise, return 0.
    """
    return spellHasDamage(s) * (getBaseDamage(s) + getVariableDamage(s, AP, AD))

"""
Returns the base damage of the spell s at max rank.
"""
def getBaseDamage(s):
    baseDamage = 0                                                  # Initialize base damage to zero
    if (s.getEffect() is not None):                                 # If my spell has an effect...
        if ((s.getEffect())[1] is not None):                        # If the first effect of the spell exists..
            baseDamage = (s.getEffect())[1][s.getMaxRank() - 1]     # Get the first effect at max rank, which contains the base damage for MOST spells.
    print(baseDamage)
    return baseDamage                                               # Returns the base damage, or returns 0 if no effect was found.

"""
Checks if the spell s does damage by checking its variables. Returns 1 if it does and 0 if it doesn't.
"""
def spellHasDamage(s):
    if s.getVars() is None: return 0            # If the spell has no variables, the spell is assumed to not do damage.
    for var in s.getVars():                     # For every variable in the spell's list of variables..
        if "damage" in (var["link"]).lower():   # Check if the word "damage" exists in the description of this spell variable.
            return 1                            # If it does, the spell is assumed to do damage and returns 1.
    return 0                                    # Otherwise, no "damage" was found, we assume the spell does no damage and return 0.

"""
Calculates the variable damage of the spell s based on variables such as % Bonus AD and % Bonus AP.
Ignores other factors.
"""
def getVariableDamage(s, AP, AD):
    variableDamage = 0                                      # Initialize variable damage to 0
    if (s.getVars() is None): return 0                      # Check if variables exist. If not, there is no variable damage.
    for var in (s.getVars()):                               # For every variable in the list of variables
        if ("spelldamage" in (var["link"]).lower()):        # If this variable corresponds to "spell damage", it scales with AP
            AP_coeff = var["coeff"][0]                      # Returns the AP scaling of this variable
            float(AP_coeff)                                 # Convert the AP scaling into a decimal
            variableDamage += (AP * AP_coeff)               # Calculate % AP * AP and add it to our variable damage.

        if "attackdamage" in (var["link"]).lower():         # If this variable corresponds to "attack damage", it scales with AD
            AD_coeff = var["coeff"][0]                      # Returns the AD scaling
            float(AD_coeff)                                 # Convert the AD scaling into a decimal
            variableDamage += (AD * AD_coeff)               # Calculate % AD * AD and add it to our variable damage.
    return variableDamage                                   # Return our variable damage once we are done.

"""
Calculates the final cooldown of the spell s with CDR taken into account, at max rank.
"""
def getSpellCooldown(s, CDR):
    cooldown = (1 - CDR) * (s.getCooldown())[s.getMaxRank() - 1]        # Net cooldown = (1 - CDR) * Initial cooldown
    cooldown = handleCooldownCases(s, cooldown, CDR)                    # Handle some edge cases based on assumptions made.
    return cooldown                                                     # Return the final cooldown

"""
Calculates the spell that has the highest score using the Riot API and the above functions.
Returns a list corresponding to this spell as : [Champion Name, Spell Name, Spell Key, Spell Description, Reason]
"""
def getHighestScore(data, AP, AD, CDR):
    highScore = 0                                               # Initialize the highest score to 0
    highChampion = ""                                           # Initialize champion name
    highSpellKey = ""                                           # Initialize spell key
    highSpellName = ""                                          # Initialize spell name
    highSpellDesc = ""                                          # Initialize spell description

    for key in data["keys"]:                                    # For every champion key
        c = Champion(data, key)                                 # Create a champion using this key and Riot API data
        print(c.getName())

        for s in c.getSpells():                                 # For every spell that belongs to this champion...
            spell = Spell(s)                                    # Create a spell object out of this spell dictionary
            print(spell.getName())
            currScore = getSpellScore(spell, AP, AD, CDR)       # Calculate the efficiency score of this spell
            print(str(currScore))
            if currScore > highScore:                           # If this spell's score is higher than the highest score..
                highScore = currScore                           # Set the high score to this spell's score
                highSpellKey = spell.getKey()                   # Set the key to this spell's key
                highSpellName = spell.getName()                 # Set the name to this spell's name
                highChampion = c.getName()                      # Set the champion name to this champion's name
                highSpellDesc = spell.getDescription()          # Set the description to this spell's description

    print(
        "Your results have been calculated based on: " + str(AP) + " AP, " + str(AD) + " AD, " + str(
            CDR * 100) + "% CDR.")
    print("Result: ")
    print("Champion: " + highChampion)
    print("Spell: " + highSpellName)
    print("Spell description: " + highSpellDesc)
    reason = "Reason: This spell has achieved a high score of: " + str(highScore) + "."  # Create a string that shows us the reason
    return [highChampion, highSpellName, highSpellKey, highSpellDesc, reason]            # Return a list corresponding to most efficient spell
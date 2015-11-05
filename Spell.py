"""
A League of Legends spell class which contains a name, key, description max rank, cooldown, cost,
variables (such as AP and AD ratios) and effects and is created from a parsed Riot API spell dictionary.
"""


class Spell:
    def __init__(self, data):
        """
        Fetches the name of the spell from the Riot API.
        """
        self.name = data["name"]

        """
        Fetches the spell key from the Riot API.
        """
        self.key = data["key"]

        """
        Fetches the spell description from the Riot API.
        """
        self.description = data["description"]

        """
        Finds the max rank of the spell and returns an integer.
        """
        self.maxrank = int(data["maxrank"])

        """
        Finds the cooldown of the spell at each rank as a list.
        """
        self.cooldown = data["cooldown"]

        """
        If the spell has an effect field, it fetches the list of effects.
        """
        if ("effect" in data):
            self.effect = data["effect"]
        else:
            self.effect = None

        """
        Finds the cost type of the spell, e.g. Mana, Energy, etc.
        """
        self.costType = data["costType"]

        """
        Finds spell variables such as AP and AD scaling if the spell contains them.
        """
        if ("vars" in data):
            self.vars = data["vars"]
        else:
            self.vars = None

        """
        Finds the cost of the spell at each rank and returns a list.
        """
        self.cost = data["cost"]

    """
    Methods to return the fields listed above.
    """

    def getName(self):
        return self.name

    def getKey(self):
        return self.key

    def getDescription(self):
        return self.description

    def getMaxRank(self):
        return self.maxrank

    def getCooldown(self):
        return self.cooldown

    def getEffect(self):
        return self.effect

    def getCostType(self):
        return self.costType

    def getVars(self):
        return self.vars

    def getCost(self):
        return self.cost

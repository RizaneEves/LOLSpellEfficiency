"""
A League of Legends champion class that contains a name and a list of spells.
The data is extracted from the parsed Riot API champion data and a champion key.
"""


class Champion:
    def __init__(self, data, key):
        """
        Gets the champion name by fetching the corresponding name to the given key from the Riot API champion data
        """
        self.name = data["keys"][key]

        """
        Gets the list of spells as a dictionary,  of the champion from the Riot API champion data
        """
        self.spells = data["data"][self.name]["spells"]

    """
    Returns the champion's name.
    """
    def getName(self):
        return self.name

    """
    Returns the champion's list of spells
    """
    def getSpells(self):
        return self.spells



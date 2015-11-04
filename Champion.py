class Champion:
    def __init__(self, data, key):
        self.name = data["keys"][key]
        self.spells = data["data"][self.name]["spells"]

    def getName(self):
        return self.name

    def getSpells(self):
        return self.spells

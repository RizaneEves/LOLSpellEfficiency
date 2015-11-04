from ImageHandler import getChampionImage


class Champion:
    def __init__(self, data, key):
        self.name = data["keys"][key]
        self.spells = data["data"][self.name]["spells"]
        self.image = getChampionImage(self.name)

    def getName(self):
        return self.name

    def getSpells(self):
        return self.spells

    def getImage(self):
        return self.image

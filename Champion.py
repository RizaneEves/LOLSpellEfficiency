class Champion(object)
    def _init_(self, data, key):
        self.name = data[key]["name"]
        self.spells = data[key]["spells"]

    def getName(self):
        return self.name

    def getSpells(self):
        return self.spells

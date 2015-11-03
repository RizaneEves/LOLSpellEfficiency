class Spell(object)
    def _init_(self, data):
        self.name = data["name"]
        self.key = data["key"]
        self.description = data["description"]
        self.maxrank = int(data["maxrank"])
        self.cooldown = float(data["cooldown"])
        self.effect = data["effect"]
        self.costType = data["costType"]
        self.vars = data["vars"]
        self.cost = data["cost"]

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
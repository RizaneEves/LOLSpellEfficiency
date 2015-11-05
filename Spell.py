


class Spell:
    def __init__(self, data):
        self.name = data["name"]
        self.key = data["key"]
        self.description = data["description"]
        self.maxrank = int(data["maxrank"])
        self.cooldown = data["cooldown"]
        if ("effect" in data):
            self.effect = data["effect"]
        else:
            self.effect = None
        self.costType = data["costType"]
        if ("vars" in data):
            self.vars = data["vars"]
        else:
            self.vars = None
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

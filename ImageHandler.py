import json
import urllib2
from PIL import Image
import requests
from StringIO import StringIO


def getLatestVersion():
    versionsURL = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key=8e8904b4-c112-4b0f-bd1e-641649d9e569'
    versions = json.load(urllib2.urlopen(versionsURL))
    return versions[0]


def getChampionImage(name):
    championURL = "http://ddragon.leagueoflegends.com/cdn/" + getLatestVersion() + "/img/champion/" + name + ".png"
    champion = requests.get(championURL)
    champImage = Image.open(StringIO(champion.content))
    return champImage


def getSpellImage(key):
    spellURL = "http://ddragon.leagueoflegends.com/cdn/" + getLatestVersion() + "/img/spell/" + key + ".png"
    spell = requests.get(spellURL)
    spellImage = Image.open(StringIO(spell.content))
    return spellImage

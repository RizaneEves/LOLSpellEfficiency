import json
import urllib2
from PIL import Image
import requests
from StringIO import StringIO

"""
This file is our image handler for our GUI. It consults the Data Dragon and receives relevant champion and spell images
from it.
"""


"""
Return the latest version of the Riot API / Data Dragon by consulting "versions" in static-data.
"""
def getLatestVersion():
    """
    Parse the versions URL and return the latest version.
    """
    versionsURL = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/versions?api_key=8e8904b4-c112-4b0f-bd1e-641649d9e569'
    versions = json.load(urllib2.urlopen(versionsURL))
    return versions[0]


"""
Retrieves the image of a champion from the Data Dragon given the champion name.
"""
def getChampionImage(name):
    """
    Parse the URL that contains the desired champion's image and return this image.
    """
    championURL = "http://ddragon.leagueoflegends.com/cdn/" + getLatestVersion() + "/img/champion/" + name + ".png"
    champion = requests.get(championURL)
    champImage = Image.open(StringIO(champion.content))
    return champImage

"""
Retrieves the image of a spell from the Data Dragon given the spell key.
"""
def getSpellImage(key):
    """
    Parse the URL that contains the desired spell's image and return this image.
    """
    spellURL = "http://ddragon.leagueoflegends.com/cdn/" + getLatestVersion() + "/img/spell/" + key + ".png"
    spell = requests.get(spellURL)
    spellImage = Image.open(StringIO(spell.content))
    return spellImage

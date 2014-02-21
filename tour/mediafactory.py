import json
from kivy.logger import Logger


def readPlaylist(fileName):
    """Returns the data of the given JSON file.
    """
    with open(fileName, 'r') as pl:
        return json.load(pl)

def loadMedia(mediaDir, playlistFile):
    """Gathers media files according to the given playlist.
    """
    try:
        playlist = readPlaylist(playlistFile)
    except IOError as e:
        msg = "Cannot load playlist: {0}"
        Logger.error(msg.format(e))
        return []

    #TODO: Continue here
    media = []
    return media

def createWidgets(playlistFile, mediaDir):
    """Creates widgets based on the given data.
    """
    media = loadMedia(playlistFile, mediaDir)
    return []

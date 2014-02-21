import json
from os import path
from collections import namedtuple
from operator import itemgetter

from kivy.logger import Logger
from kivy.uix.image import Image


MediaObject = namedtuple("MediaObject", ["name", "widget", "thumbnail"])


def readPlaylist(fileName):
    """Returns the data of the given JSON file.
    """
    with open(fileName, 'r') as pl:
        return json.load(pl)


def loadMedia(mediaDir, playlistFile):
    """Gathers media files according to the given playlist.
    """
    try:
        playlist = readPlaylist(path.join(mediaDir, playlistFile))
    except IOError as e:
        msg = "Cannot load playlist: {0}"
        Logger.error(msg.format(e))
        return []

    getData = itemgetter('type', 'name', 'source', 'thumbnail')
    for mType, name, src, thumb in map(getData, playlist):
        thumb = Image(source=path.join(mediaDir, thumb))
        widget = createWidget(mType, path.join(mediaDir, src))
        tmp = MediaObject(name, widget, thumb)
    
    media = []
    return media


def createWidget(widgetType, widgetData):
    """Create a widget based on the given data.
    """
    return None

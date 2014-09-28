import json
from os import path
from collections import namedtuple
from operator import itemgetter

from kivy.logger import Logger
from gallery.scene import Scene
from gallery.walkaround import Walkaround
from gallery.still import Still


MediaObject = namedtuple("MediaObject", ["name", "widget", "thumbnail", "featured"])


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

    getData = itemgetter('type', 'name', 'source', 'thumbnail', 'featured')

    media = []
    for mType, name, src, thumb, feat in map(getData, playlist):
        thumb = path.join(mediaDir, thumb)
        feat = path.join(mediaDir, feat)
        widget = createWidget(mType, path.join(mediaDir, src))
        media.append(MediaObject(name, widget, thumb, feat))
    return media


widgetClasses = {'Walkaround': Walkaround, 'Still': Still, 'Scene': Scene}

def createWidget(widgetType, widgetData):
    """Create a widget based on the given data.
    """
    return widgetClasses.get(widgetType)(widgetData)

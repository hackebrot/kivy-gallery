from random import randint

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.properties import ObjectProperty


class Explorer(FloatLayout):
    """Layout displaying all MediaObjects. Features multitouch transformations.
    """
    def __init__(self, media):
        super(Explorer, self).__init__()
        for mediaObject in media:
            item = ExplorerItem(mediaObject)
            self.add_widget(item)


class ExplorerItem(Scatter):
    """Scatter showing a featured image for each MediaObject used throughout the app.
    """
    screenMgr = ObjectProperty()
    image = ObjectProperty()

    def __init__(self, mediaObject):
        super(ExplorerItem, self).__init__()
        self.mediaObject = mediaObject
        self.image.source = self.mediaObject.featured
        self.rotation = 10 * randint(-2, 2)
        self.pos = (self.x + randint(-200, 200), self.y + randint(-150 , 150))

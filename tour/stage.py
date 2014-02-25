from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty


class Stage(AnchorLayout):
    """Layout showing a single MediaObject.
    """
    content = ObjectProperty()

    def __init__(self, media):
        super(Stage, self).__init__()
        for mediaObject in media:
            self.content.add_widget(mediaObject.widget)
        self.objIndices = dict((obj, i) for i, obj in enumerate(media))

    def show(self, mediaObject):
        """Shows the slide containing the given mediaObject.
        """
        self.content.index = self.objIndices.get(mediaObject)


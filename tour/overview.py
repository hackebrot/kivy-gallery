from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty


class Overview(ScrollView):
    """ScrollView showing all media widgets available in the app.
    """
    content = ObjectProperty()

    def __init__(self, media):
        super(Overview, self).__init__()
        for mediaObject in media:
            item = OverviewItem(mediaObject)
            self.content.add_widget(item)


class OverviewItem(Button):
    """Button representing a mediaObject in the overview
    and displaying its name and thumbnail respectively.
    """
    screenMgr = ObjectProperty()

    def __init__(self, mediaObject):
        super(OverviewItem, self).__init__()
        self.mediaObject = mediaObject
        self.text = self.mediaObject.name
        self.background_normal = self.mediaObject.thumbnail

    def on_press(self):
        self.screenMgr.showMediaObject(self.mediaObject)



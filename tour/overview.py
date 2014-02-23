from functools import partial

from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty


class Overview(ScrollView):
    """ScrollView showing all media widgets available in the app.
    """
    content = ObjectProperty()

    def __init__(self, media, action):
        super(Overview, self).__init__()
        for mediaObject in media:
            item = OverviewItem(mediaObject.name, mediaObject.thumbnail)
            item.bind(on_press=partial(action, mediaObject))
            self.content.add_widget(item)


class OverviewItem(Button):
    """Button representing a mediaObject in the overview
    and displaying its name and thumbnail respectively.
    """
    def __init__(self, name, thumbnail):
        super(OverviewItem, self).__init__()
        self.text = name
        self.background_normal = thumbnail



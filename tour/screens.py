from functools import partial

from kivy.logger import Logger
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class ScreenMgr(ScreenManager):
    """Custom ScreenManager providing callbacks for switching screens.
    """
    transition = FadeTransition()

    def __init__(self, media):
        super(ScreenMgr, self).__init__()
        self.overview = SideBarScreen("Overview", Overview(media, self.showMediaObject))
        self.stage = SideBarScreen("Stage", Button(text="Stage"))
        self.explorer = SideBarScreen("Explorer", Button(text="Explorer"))
        self.addScreens(self.overview, self.stage, self.explorer)

    def addScreens(self, *screens):
        """Adds the given screens and populates the sidebars respectively.
        """
        for scrn in screens:
            self.add_widget(scrn)
            scrn.setupActions((self.setCurrentScreen, s) for s in screens)

    def setCurrentScreen(self, screen, *args):
        """Displays the given screen. Uses args in definition to
        handle the incoming btn instance.
        """
        self.current = screen.name

    def showMediaObject(self, mediaObj, *args):
        """Callback for any buttons and a like requesting a mediaObject to be shown.
        """
        Logger.info("Requested MediaObject {0}".format(mediaObj))
        self.setCurrentScreen(self.stage)


class SideBarScreen(Screen):
    """Screen containing a SideBar in addition to its featured widget.
    """
    menu = ObjectProperty()
    lbl = ObjectProperty()
    content = ObjectProperty()

    def __init__(self, name, content):
        super(SideBarScreen, self).__init__(name=name)
        self.content.add_widget(content)

    def on_pre_leave(self):
        """Assures that the menu is reset on a screen transition.
        """
        super(SideBarScreen, self).on_pre_leave()
        self.lbl.collapse()

    def setupActions(self, actions):
        """Connects the menu with the given actions.
        """
        for action, screen in actions:
            self.menu.setupAction(screen.name, partial(action, screen))


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


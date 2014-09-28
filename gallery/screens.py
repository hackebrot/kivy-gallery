from functools import partial

from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from gallery.overview import Overview
from gallery.stage import Stage
from gallery.explorer import Explorer


class ScreenMgr(ScreenManager):
    """Custom ScreenManager providing callbacks for switching screens.
    """
    transition = FadeTransition()

    def __init__(self, media):
        super(ScreenMgr, self).__init__()
        self.overviewScreen = SideBarScreen("Overview", Overview(media))
        self.explorerScreen = SideBarScreen("Explorer", Explorer(media))

        self.stage = Stage(media)
        self.stageScreen = SideBarScreen("Stage", self.stage)

        self.addScreens(self.overviewScreen, self.stageScreen, self.explorerScreen)

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
        """Callback for any buttons and a like requesting a mediaObject
        to be shown on the stage.
        """
        Logger.info("Requested MediaObject {0}".format(mediaObj))
        self.setCurrentScreen(self.stageScreen)
        self.stage.show(mediaObj)


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



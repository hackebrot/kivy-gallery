from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class ScreenMgr(ScreenManager):
    transition = FadeTransition()

    def __init__(self):
        super(ScreenMgr, self).__init__()
        self.add_widget(Overview())
        self.add_widget(Stage())
        self.add_widget(Explorer())

        for scrn in self.screens:
            scrn.setupActions((self.setCurrentScreen, s) for s in self.screens)

    def setCurrentScreen(self, screen, *args):
        """Displays the given screen. Uses args in definition to
        handle the incoming btn instance.
        """
        self.current = screen.name


class SideBarScreen(Screen):
    """Screen containing a SideBar in addition to its featured widget.
    """
    menu = ObjectProperty()
    lbl = ObjectProperty()

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


class Overview(SideBarScreen):
    """BaseScreen showing all media widgets available in the app.
    """
    pass

class Stage(SideBarScreen):
    """BaseScreen for viewing a single media item at a time.
    """
    pass

class Explorer(SideBarScreen):
    """BaseScreen showing previously displayed media items.
    """
    pass


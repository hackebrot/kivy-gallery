from functools import partial

from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class ScreenMgr(ScreenManager):
    transition = FadeTransition()

    def __init__(self):
        super(ScreenMgr, self).__init__()
        self.add_widget(SideBarScreen("Overview", Label(text="Overview")))
        self.add_widget(SideBarScreen("Stage", Label(text="Stage")))
        self.add_widget(SideBarScreen("Explorer", Label(text="Explorer")))

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


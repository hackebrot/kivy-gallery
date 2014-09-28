from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SideBarMenu(BoxLayout):
    """Menu providing buttons for switching the screens.

    Since widgets cannot be assigned to multiple parents,
    each screen has its own menu.
    """

    def setupAction(self, title, action):
        """Adds a button based on the given data.
        """
        self.add_widget(SideBarButton(text=title, on_press=action))
                               

class SideBarButton(Button):
    pass

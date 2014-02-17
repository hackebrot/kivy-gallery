from kivy.app import App
from tour.screens import ScreenMgr


class TourApp(App):
    def build(self):
        return ScreenMgr()

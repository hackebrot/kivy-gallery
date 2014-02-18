from os import path
from kivy.app import App
from tour.screens import ScreenMgr


class TourApp(App):
    def build_config(self, config):
        config.adddefaultsection('media')
        config.setdefault('media', 'dir', 'media')
        config.setdefault('media', 'playlist', 'playlist.json')

    def build(self):
        self.mediaDir = self.config.get('media', 'dir')
        self.playlist = self.config.get('media', 'playlist')
        return ScreenMgr()

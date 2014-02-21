from kivy.app import App
from tour.screens import ScreenMgr
from tour.mediafactory import loadMedia


class TourApp(App):
    def build_config(self, config):
        config.adddefaultsection('media')
        config.setdefault('media', 'dir', 'media')
        config.setdefault('media', 'playlist', 'playlist.json')

    def build(self):
        mediaDir = self.config.get('media', 'dir')
        playlistFile = self.config.get('media', 'playlist')

        widgets = loadMedia(mediaDir, playlistFile)

        return ScreenMgr()

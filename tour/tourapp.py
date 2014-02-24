import kivy
kivy.require('1.8.0')
from kivy.config import Config
appWidth, appHeight = 960, 540
Config.set('graphics', 'width', appWidth)
Config.set('graphics', 'height', appHeight)
#Use this to set the size of the app as suggested at:
#https://groups.google.com/forum/#!topic/kivy-users/TR7UycgcLpQ

from kivy.app import App
from kivy.properties import ObjectProperty
from tour.screens import ScreenMgr
from tour.mediafactory import loadMedia


class TourApp(App):
    mgr = ObjectProperty()

    def build_config(self, config):
        config.adddefaultsection('media')
        config.setdefault('media', 'dir', 'media')
        config.setdefault('media', 'playlist', 'playlist.json')

    def build(self):
        mediaDir = self.config.get('media', 'dir')
        playlistFile = self.config.get('media', 'playlist')

        media = loadMedia(mediaDir, playlistFile)

        #Store the app's window size for straightforward references
        self.size = self.width, self.height = appWidth, appHeight  

        self.mgr = ScreenMgr(media)
        return self.mgr

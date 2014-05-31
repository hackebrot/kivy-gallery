import kivy
kivy.require('1.8.0')
from kivy.config import Config
Config.set('graphics', 'width', 1920)
Config.set('graphics', 'height', 1080)
#Use this to set the size of the app as suggested at:
#https://groups.google.com/forum/#!topic/kivy-users/TR7UycgcLpQ

from os import path
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from tour.screens import ScreenMgr
from tour.mediafactory import loadMedia


class TourApp(App):
    mgr = ObjectProperty()

    def build_config(self, config):
        config.adddefaultsection('media')
        config.setdefault('media', 'dir', 'media')
        config.setdefault('media', 'playlist', 'playlist.json')
        config.setdefault('media', 'music', 'music.ogg')

    def build(self):
        mediaDir = self.config.get('media', 'dir')
        playlistFile = self.config.get('media', 'playlist')
        musicFile = self.config.get('media', 'music')

        sound = SoundLoader.load(path.join(mediaDir, musicFile))
        sound.loop = True
        sound.play()

        media = loadMedia(mediaDir, playlistFile)
        self.mgr = ScreenMgr(media)

        return self.mgr

import kivy
kivy.require('1.8.0')
from kivy.config import Config
Config.set('graphics', 'width', 960)
Config.set('graphics', 'height', 540)
#Use this to set the size of the app as suggested at:
#https://groups.google.com/forum/#!topic/kivy-users/TR7UycgcLpQ

from os import path
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from gallery.screens import ScreenMgr
from gallery.mediafactory import loadMedia


class GalleryApp(App):
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

        mediaDir = path.realpath(mediaDir)
        sound = SoundLoader.load(path.join(mediaDir, musicFile))
        sound.loop = True
        sound.play()

        media = loadMedia(mediaDir, playlistFile)
        self.mgr = ScreenMgr(media)

        return self.mgr

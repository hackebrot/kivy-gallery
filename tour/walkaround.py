from os import path
from glob import glob

from kivy.uix.image import AsyncImage
from kivy.uix.floatlayout import FloatLayout


class Walkaround(FloatLayout):
    """Widget providing intuitive controls for exploring
    a sequence of lazy loaded images.
    """
    current = 0

    def __init__(self, imgDir):
        super(Walkaround, self).__init__()
        self.loadImages(path.join(imgDir, '*'))
        self.updateImage(0)

    def loadImages(self, imgDir):
        """Create an AsyncImage instance for each file in the given folder.
        """
        fNames = sorted(glob(imgDir))
        self.images = list(AsyncImage(source=fn) for fn in fNames)

    def updateImage(self, idx):
        """Display the image at index and store the index.
        """
        self.clear_widgets()
        self.add_widget(self.images[idx])
        self.current = idx

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return super(Walkaround, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        """Change the image on user interaction based on the movements speed.
        """
        if touch.grab_current is self:
            step = int(touch.dx / 5)
            self.updateImage((self.current - step) % len(self.images))


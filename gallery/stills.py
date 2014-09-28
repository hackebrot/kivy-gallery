from itertools import cycle

from kivy.uix.image import Image
from kivy.logger import Logger


class Stills(Image):
    """Animated image showing a number of stills.
    """
    delayRange = cycle(pow(2, _) for _ in range(2, -1, -1))

    def __init__(self, zipFile):
        super(Stills, self).__init__(source=zipFile)
        self.changeDelay()

    def changeDelay(self):
        """Sets the delay to next in the sequence of 4, 2, 1, 0.5.
        """
        self.anim_delay = next(self.delayRange)
        Logger.info("New anim_delay: {0}".format(self.anim_delay))

    def on_touch_down(self, touch):
        """Adjust the speed in which images are switched.
        """
        if self.collide_point(*touch.pos):
            self.changeDelay()
            return True

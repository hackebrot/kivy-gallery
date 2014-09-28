from kivy.uix.video import Video


class Scene(Video):
    """Custom Video showing the given file.
    """
    def __init__(self, videoFile):
        super(Scene, self).__init__(source=videoFile)
        self.state = 'play'
        self.eos = 'loop'

    def toggleState(self):
        self.state = 'pause' if self.state == 'play' else 'play'

    def on_touch_down(self, touch):
        """Simply toggle between pause and play.
        """
        if self.collide_point(*touch.pos):
            self.toggleState()
            return True


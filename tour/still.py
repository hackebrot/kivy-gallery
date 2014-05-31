from kivy.uix.image import Image


class Still(Image):
    def __init__(self, fileName):
        super(Still, self).__init__(source=fileName)

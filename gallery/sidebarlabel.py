from kivy.uix.label import Label
from kivy.animation import Animation


class SideBarLabel(Label):
    """A draggable label which is used in the SideBar.

    Based on http://blog.tshirtman.fr/2012/10/22/kivy-android-like-pulldown-menu
    """
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        return super(SideBarLabel, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            self.y = touch.y
            return True
        return super(SideBarLabel, self).on_touch_move(touch)

    def collapse(self):
        Animation(top=self.parent.top, duration=0.3).start(self)

    def expand(self):
        Animation(y=0 + self.parent.height * 0.8, duration=0.3).start(self)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            if touch.dy > 0:
                self.collapse()
            else:
                self.expand()
            return True
        return super(SideBarLabel, self).on_touch_up(touch)

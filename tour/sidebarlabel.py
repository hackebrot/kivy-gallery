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
            self.x = touch.x
            return True
        return super(SideBarLabel, self).on_touch_move(touch)

    def collapse(self):
        Animation(x=0, duration=0.3).start(self)

    def expand(self):
        Animation(right=self.parent.right * 0.2, duration=0.3).start(self)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            if touch.dx < 0:
                self.collapse()
            else:
                self.expand()
            return True
        return super(SideBarLabel, self).on_touch_up(touch)

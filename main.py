#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from gallery.galleryapp import GalleryApp
from gallery.sidebarlabel import SideBarLabel
from gallery.sidebarmenu import SideBarMenu
from gallery.screens import ScreenMgr


if __name__ in ('__main__', '__android__'):
    GalleryApp().run()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# by Radek Liska, 2019
#

import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import GObject, Nautilus, Gtk


def ok():
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.tab-previous", ["<shift><control>Tab", "<control>Page_Up"])
    app.set_accels_for_action("win.tab-next", ["<control>Tab", "<control>Page_Down"])


class CtrlTabSwitch(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(self):
        pass

    def get_widget(self, uri, window):
        ok()
        return None

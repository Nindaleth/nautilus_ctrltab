# Nautilus CtrlTab Extension
#
# use ctrl+tab and ctrl+shift+tab to change tabs (in addition to the existing shortcuts)
#

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Gtk


def ok():
    app = Gtk.Application.get_default()
    app.set_accels_for_action("win.tab-previous", ["<shift><control>Tab", "<control>Page_Up"])
    app.set_accels_for_action("win.tab-next", ["<control>Tab", "<control>Page_Down"])


class CtrlTabSwitch(GObject.GObject):
    def __init__(self):
        pass

    def get_widget(self, uri, window):
        ok()
        return None

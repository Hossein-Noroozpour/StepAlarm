from mako.template import _get_module_info_from_callable

__author__ = 'Hossein Noroozpour'
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Step Alarm")
        grid = Gtk.Grid()
        self.add(grid)


if '__main__' == __name__:
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
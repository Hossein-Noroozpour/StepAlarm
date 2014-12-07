__author__ = 'Hossein Noroozpour'
import subprocess

from gi.repository import Gtk, GLib


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Step Alarm")
        self.mins = 0
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        grid = Gtk.Grid()
        self.add(grid)
        al = Gtk.Label("Alarm in next")
        grid.attach(al, 0, 0, 1, 1)
        self.ea = Gtk.Entry()
        self.ea.set_text("minutes")
        grid.attach(self.ea, 1, 0, 1, 1)
        ml = Gtk.Label("Music")
        grid.attach(ml, 0, 1, 1, 1)
        self.mf = Gtk.FileChooserButton("Music file location")
        grid.attach(self.mf, 1, 1, 1, 1)
        self.sb = Gtk.Button("Start")
        self.sb.connect("clicked", self.on_start)
        grid.attach(self.sb, 0, 2, 1, 1)
        self.cb = Gtk.Button("Cancel")
        self.cb.connect("clicked", self.on_cancel)
        self.cb.set_sensitive(False)
        grid.attach(self.cb, 1, 2, 1, 1)
        self.timer = None
        self.file = None

    def on_start(self, button):
        print("started.")
        try:
            mins = int(self.ea.get_text())
        except ValueError:
            msg = Gtk.MessageDialog(self,
                                    Gtk.DialogFlags.DESTROY_WITH_PARENT,
                                    Gtk.MessageType.ERROR,
                                    Gtk.ButtonsType.CLOSE,
                                    "You Entered wrong number for Minute.")
            msg.run()
            msg.destroy()
            return
        self.file = self.mf.get_filename()
        if None == self.file:
            msg = Gtk.MessageDialog(self, Gtk.DialogFlags.DESTROY_WITH_PARENT, Gtk.MessageType.ERROR,
                                    Gtk.ButtonsType.CLOSE, "You did specify any music file.")
            msg.run()
            msg.destroy()
            return
        print("Music file is: " + self.file)
        print("Minute is: " + str(mins))
        self.sb.set_sensitive(False)
        self.cb.set_sensitive(True)
        self.timer = GLib.timeout_add_seconds(60, self.on_timer)
        self.mins = mins

    def on_timer(self):
        print("Alarm")
        self.mins -= 1
        if self.mins < 0:
            self.sb.set_sensitive(True)
            self.cb.set_sensitive(False)
            subprocess.call(['vlc', self.file])
            return False
        else:
            print(self.mins, " min left.")
            return True

    def on_cancel(self, button):
        print("Canceled.")
        GLib.source_remove(self.timer)
        self.sb.set_sensitive(True)
        self.cb.set_sensitive(False)


if '__main__' == __name__:
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
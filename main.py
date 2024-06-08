import os
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


APPID = 'com.github.taniyoshima.pyt_gtk4_aboutdialog'


@Gtk.Template(filename=os.path.dirname(__file__) + '/ui_file.ui')
class Gtk4TestTest(Gtk.ApplicationWindow):

    __gtype_name__ = "window"

    menubutton = Gtk.Template.Child()
    menu = Gtk.Template.Child()
    aboutdialog = Gtk.Template.Child()

    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, application=app)

        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about_clicked)
        self.add_action(action)

        popover = Gtk.PopoverMenu.new_from_model(self.menu)
        self.menubutton.set_popover(popover)

    def on_about_clicked(self, action, param):
        self.aboutdialog.set_visible(True)

    @Gtk.Template.Callback()
    def on_dialog_closereq(self, dialog):
        dialog.set_visible(False)
        return True


class Gtk4TestApp(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id=APPID)

    def do_activate(self):
        window = Gtk4TestTest(self)
        window.present()


def main():
    app = Gtk4TestApp()
    app.run()


if __name__ == '__main__':
    main()

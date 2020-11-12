import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class PrimeiraFiestraGlade ():
    def __init__(self):
        builder = Gtk.Builder ()
        builder.add_from_file ("primeiraFiestraGlade.glade")

        sinais = { "gtk_main_quit": self.on_pechar
        }
        winFiestraPrincipal = builder.get_object ("winFiestraPrincipal")
        winFiestraPrincipal.show_all()

    def on_pechar (self):
        Gtk.main_quit()


if __name__ == "__main__":
    PrimeiraFiestraGlade ()
    Gtk.main()
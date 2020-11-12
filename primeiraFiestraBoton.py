import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class PrimeiraFiestraBoton (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title ("Exemplo de Gtk.Window")
        self.set_default_size ( 300,200)

        btnBotonSaida = Gtk.Button()
        btnBotonSaida.set_label ("Sair")
        btnBotonSaida.connect ("clicked", self.on_btnBotonSaida_clicked, "Datos de usuario que eu estime oportunos")

        self.add (btnBotonSaida)

        self.connect ('delete-event', Gtk.main_quit)
        self.show_all ()

    def on_btnBotonSaida_clicked (self, control, datos):
        print (datos)
        Gtk.main_quit ()

if __name__ == "__main__":
    PrimeiraFiestraBoton ()
    Gtk.main()
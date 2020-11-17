import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class SaudoPOO (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Saudo mediante POO")
        self.set_size_request (200, 100)

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add (caixaV)

        self.lblSaudo = Gtk.Label (label = "Escribe o teu nome")
        caixaV.pack_start( self.lblSaudo, True, True, 2)

        self.txtSaudo = Gtk.Entry (text ="Escribe aqui o teu nome")
        self.txtSaudo.connect ("activate", self.on_btnSaudo_clicked)
        caixaV.pack_start (self.txtSaudo, True, False, 2)

        self.btnSaudo = Gtk.Button (label = "Saudo")
        self.btnSaudo.connect ("clicked", self.on_btnSaudo_clicked)
        caixaV.pack_start (self.btnSaudo, False, False, 2)


        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()




    def on_btnSaudo_clicked (self, boton):
        nome = self.txtSaudo.get_text()
        if nome != "":
            self.lblSaudo.set_text ("Ola " + nome + ". Benvido!!!")
            self.txtSaudo.set_text ("")

    """def on_txtSaudo_activate(self, cadroTexto):
        self.on_btnSaudo_clicked(cadroTexto)
    """
if __name__ == "__main__":
    SaudoPOO ()
    Gtk.main()
import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class SaudoGtkBox (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Saudo mediante POO e deseño de interface mediante Gtk.Box")
        self.set_size_request (200, 100)

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add (caixaV)



        self.lblSaudo = Gtk.Label (label = "Escribe o teu nome")
        caixaV.pack_start( self.lblSaudo, True, True, 2)

        self.txtSaudo = Gtk.Entry (text ="Escribe aqui o teu nome")
        self.txtSaudo.connect ("activate", self.on_btnSaudo_clicked, "saudo")
        caixaV.pack_start (self.txtSaudo, True, False, 2)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        caixaV.pack_start (caixaH, True, True, 2)

        self.btnSaudo = Gtk.Button (label = "Saudo")
        self.btnSaudo.connect ("clicked", self.on_btnSaudo_clicked, "saudo")
        caixaH.pack_start (self.btnSaudo, True, False, 2)

        self.btnDespedida = Gtk.Button (label = "Despedida")
        self.btnDespedida.connect ("clicked", self.on_btnSaudo_clicked, "despedida")
        caixaH.pack_start (self.btnDespedida, True, False, 2)


        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()



    def on_btnSaudo_clicked (self, boton, tipo):
        nome = self.txtSaudo.get_text()
        if nome != "":
            if tipo == "saudo":
                self.lblSaudo.set_text ("Ola " + nome + ". Benvido!!!")
                self.txtSaudo.set_text ("")
            elif tipo == "despedida":
                self.lblSaudo.set_text("Adeus " + nome + ". Ata pronto!!!")
                self.txtSaudo.set_text("")


    """def on_txtSaudo_activate(self, cadroTexto):
        self.on_btnSaudo_clicked(cadroTexto)
    """
if __name__ == "__main__":
    SaudoGtkBox ()
    Gtk.main()
import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class SaudoGtkGrid (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Saudo mediante POO e deseño de interface mediante Gtk.Grid")
        #self.set_size_request (200, 100)

        grid = Gtk.Grid()
        self.add (grid)

        self.lblSaudo = Gtk.Label (label = "Escribe o teu nome")
        self.txtSaudo = Gtk.Entry (text ="Escribe aqui o teu nome")
        self.btnSaudo = Gtk.Button (label = "Saudo")
        self.btnDespedida = Gtk.Button (label = "Despedida")

        grid.attach(self.lblSaudo, 0, 0, 2, 1)
        grid.attach_next_to(self.txtSaudo, self.lblSaudo, Gtk.PositionType.BOTTOM, 2, 1)
        grid.attach(self.btnSaudo, 0, 2, 1, 1)
        grid.attach_next_to(self.btnDespedida, self.btnSaudo, Gtk.PositionType.RIGHT, 1, 1)

        self.txtSaudo.connect ("activate", self.on_btnSaudo_clicked, "saudo")
        self.btnSaudo.connect("clicked", self.on_btnSaudo_clicked, "saudo")
        self.btnDespedida.connect ("clicked", self.on_btnSaudo_clicked, "despedida")
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



if __name__ == "__main__":
    SaudoGtkGrid ()
    Gtk.main()
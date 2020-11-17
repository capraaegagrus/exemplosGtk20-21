import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class SaudoGlade ():
    def __init__(self):

        builder = Gtk.Builder ()
        builder.add_from_file ("saudoGlade.glade")
        sinais = {"on_btnSaudo_clicked": self.on_btnSaudo_clicked,
                  "on_txtSaudo_activate": self.on_btnSaudo_clicked,
                  "on_winSaudo_delete_event": Gtk.main_quit}
        builder.connect_signals (sinais)

        self.txtSaudo = builder.get_object ("txtSaudo")
        self.lblSaudo = builder.get_object ("lblSaudo")

    def on_btnSaudo_clicked (self, boton):
        nome = self.txtSaudo.get_text()
        if nome != "":
            self.lblSaudo.set_text ("Ola " + nome + ". Benvido!!!")
            self.txtSaudo.set_text ("")

    """def on_txtSaudo_activate(self, cadroTexto):
        self.on_btnSaudo_clicked(cadroTexto)
    """
if __name__ == "__main__":
    SaudoGlade ()
    Gtk.main()
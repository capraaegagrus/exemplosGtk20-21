import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk, Gio




class ExemploGtkHeaderBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.HeaderBar")
        #self.set_default_size (500, 200)
        self.set_border_width (10)

        cabeceira = Gtk.HeaderBar ()
        self.set_titlebar (cabeceira)
        cabeceira.set_show_close_button(True)
        cabeceira.props.title = "Exemplo de uso Gtk.HeaderBar"

        boton1 = Gtk.Button()
        icono = Gio.ThemedIcon (name = "mail-send-receive-symbolic")
        imaxe = Gtk.Image.new_from_gicon (icono, Gtk.IconSize.BUTTON)
        boton1.add(imaxe)
        boton1.connect("clicked", self.on_boton_clicked, "reciclado")
        #boton1.connect ("clicked", self.on_boton1_clicked)
        cabeceira.pack_end (boton1)

        caixa = Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class (caixa.get_style_context(), "linked")

        #boton2 = Gtk.Button ( )
        boton2 = Gtk.Button.new_from_icon_name('pan-end-symbolic', Gtk.IconSize.MENU)
        boton2.connect("clicked", self.on_boton_clicked, "flechiña")
        #boton2.connect ("clicked", self.on_boton2_clicked)
        caixa.add(boton2)
        cabeceira.pack_start (caixa)

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy (Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.add (scroll)
        self.txvCaixaTexto = Gtk.TextView()
        scroll.add (self.txvCaixaTexto)
        #get_buffer()


        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def on_boton_clicked(self, boton, nomeBoton):
        buffer = self.txvCaixaTexto.get_buffer()
        buffer.insert_at_cursor ("Pulsado o botón "+ nomeBoton +" \n")
        


"""
    def on_boton1_clicked (self, boton):
        buffer = self.txvCaixaTexto.get_buffer()
        #buffer.insert_at_cursor ("Pulsado o botón reciclado \n")
        buffer.set_text("Pulsado o botón reciclado \n")

    def on_boton2_clicked (self, boton):
        buffer = self.txvCaixaTexto.get_buffer()
        buffer.insert_at_cursor ("Pulsando o botón flechiña \n")
"""
if __name__ == "__main__":
    ExemploGtkHeaderBar ()
    Gtk.main()
import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk


class Panel (Gtk.Grid):
    def __init__(self):

        Gtk.Grid.__init__(self)

        boton1 = Gtk.Button(label="Boton 1")
        boton2 = Gtk.Button(label="Boton 2")
        boton3 = Gtk.Button(label="Boton 3")
        boton4 = Gtk.Button(label="Boton 4")
        boton5 = Gtk.Button(label="Boton 5")
        boton6 = Gtk.Button(label="Boton 6")

        self.add(boton1)
        self.attach(boton2, 1, 0, 2, 1)
        self.attach_next_to(boton3, boton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach_next_to(boton4, boton3, Gtk.PositionType.RIGHT, 2, 1)
        self.attach(boton5, 1, 2, 1, 1)
        self.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)


class ExemploGtkNoteBook(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.Stack e Gtk.StackSwicher")
        self.set_size_request (200, 100)
        self.set_border_width (4)

        self.notebook = Gtk.Notebook()
        self.add (self.notebook)

        paxina1 = Gtk.Box()
        paxina1.set_border_width (10)
        paxina1.add (Gtk.Label (label = "Páxina inicial!"))
        self.notebook.append_page (paxina1, Gtk.Label (label="Título de texto"))

        paxina2 = Gtk.Box()
        paxina2.set_border_width (10)
        paxina2.add (Gtk.Label (label = "Páxina con unha imaxe e título"))
        self.notebook.append_page(
            paxina2,
            Gtk.Image.new_from_icon_name ("help-about", Gtk.IconSize.MENU)
        )

        panel = Panel()
        panel.set_border_width (10)
        self.notebook.append_page(panel, Gtk.Label (label="Panel de traballo"))



        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
    ExemploGtkNoteBook ()
    Gtk.main()
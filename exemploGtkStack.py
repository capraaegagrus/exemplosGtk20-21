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


class ExemploGtkStack(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.Stack e Gtk.StackSwicher")
        self.set_size_request (200, 100)

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 6)
        self.add (caixaV)

        stack = Gtk.Stack ()
        stack.set_transition_type (Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration (1000)

        botonChequeo = Gtk.CheckButton (label = "Púlsame!")
        stack.add_titled (botonChequeo, "Chequeo", "Botón de chequeo")

        stack_switcher = Gtk.StackSwitcher ()
        stack_switcher.set_stack (stack)

        etiqueta = Gtk.Label ()
        etiqueta.set_markup ("<big>Etiqueta elegante</big>")
        stack.add_titled (etiqueta, "Etiqueta", "Unha etiqueta")

        panel = Panel()
        stack.add_titled (panel, "Panel", "Panel de traballo")
        stack_switcher.set_stack (stack)
        caixaV.pack_start(stack, True, True, 0)
        caixaV.pack_start (stack_switcher, True, True, 0)






        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()



if __name__ == "__main__":
    ExemploGtkStack ()
    Gtk.main()
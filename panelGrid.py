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

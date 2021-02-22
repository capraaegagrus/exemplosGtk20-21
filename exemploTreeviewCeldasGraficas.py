import sqlite3 as dbapi

import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk



class ExemploGtkTreeViewCeldasGraficas (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.TreeView con CellRendererPixbuf")
        self.set_size_request (250, 100)

        caixa = Gtk.Box ()
        #Obxecto modelo
        modelo = Gtk.ListStore (str,str)
        modelo.append (["Novo", "document-new"])
        modelo.append(["Abrir", "document-open"])
        modelo.append(["Gardar", "document-save"])

        vista = Gtk.TreeView (model = modelo)

        celdaText = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn ("Acción", celdaText, text = 0)
        vista.append_column (columna)

        celdaImx = Gtk.CellRendererPixbuf()
        columna = Gtk.TreeViewColumn ("Icono", celdaImx, icon_name = 1)
        vista.append_column (columna)

        caixa.pack_start(vista,True, True,0)

        combo = Gtk.ComboBox()
        combo.set_model(modelo)
        combo.pack_start (celdaImx, True)
        combo.add_attribute (celdaImx, "icon_name", 1)

        caixa.pack_start (combo, True, False, 0)

        self.add (caixa)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ == "__main__":
    ExemploGtkTreeViewCeldasGraficas ()
    Gtk.main()
























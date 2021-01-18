import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk



class ExemploGtkTreeViewToogle (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.TreeView")
        self.set_size_request (250, 100)

        #Obxecto modelo
        modelo = Gtk.ListStore (str, bool)
        modelo.append (["Ethernet", True])
        modelo.append(["Wireless", True])
        modelo.append(["Bluetooth", False])
        modelo.append(["3g Mobíl", True])

        trvComunicacion = Gtk.TreeView (modelo)

        cellRendererText = Gtk.CellRendererText()

        trcColumna = Gtk.TreeViewColumn  ("Tipo conexión")
        trcColumna.pack_start (cellRendererText, False)
        trcColumna.add_attribute(cellRendererText, "text", 0)
        trvComunicacion.append_column(trcColumna)

        cellRendererToggle = Gtk.CellRendererToggle ()
        cellRendererToggle.connect ("toggled", self.on_celda_toggled, modelo)

        trcColumna = Gtk.TreeViewColumn ("Estado")
        trcColumna.pack_start (cellRendererToggle, False)
        trcColumna.add_attribute(cellRendererToggle, "active",1)
        trvComunicacion.append_column(trcColumna)

        self.add (trvComunicacion)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def on_celda_toggled (self, celda, fila, modelo):
        #modelo [fila][1] = not modelo [fila] [1]
        print ("O usuario fixo clic")


if __name__ == "__main__":
    ExemploGtkTreeViewToogle ()
    Gtk.main()
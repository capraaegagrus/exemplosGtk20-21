import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

columnas = ["Nome",
            "Apelido",
            "Número de teléfono"]

axendaTel = [["Manuel", "Gil", "986 345 678"],
             ["Ana", "Sáez", "607 891 891"],
             ["Rosa", "Cendón", "678 432 456"],
             ["Raúl", "Pérez", "651 327 453"],
             ["Óscar", "Vila", "986123 321"]]


class ExemploGtkTreeViewTelefonos (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.TreeView")
        self.set_size_request (250, 100)

        #Obxecto modelo
        mod_axenda_tel = Gtk.ListStore (str, str, str)
        for persoa in axendaTel:
            mod_axenda_tel.append (persoa)

        taboaAxenda = Gtk.TreeView (model = mod_axenda_tel)

        i=0
        for columna in columnas:
            celdaRenderer = Gtk.CellRendererText()
            col = Gtk.TreeViewColumn (columna, celdaRenderer, text=i )
            taboaAxenda.append_column (col)
            i=i+1

        self.add (taboaAxenda)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    ExemploGtkTreeViewTelefonos ()
    Gtk.main()
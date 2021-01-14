import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk




class ExemploGtkTreeViewArbore (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.TreeView")
        self.set_size_request (250, 100)

        #Obxecto modelo
        modelo = Gtk.TreeStore(str, int)

        for avo in range (5):
            idAvo = modelo.append (None, ["Avó " + str(avo), avo])
            for pai in range(4):
                idPai = modelo.append (idAvo, ["Pai % i do avó % i" % (pai, avo), pai])
                for fillo in range (3):
                    modelo.append (idPai, ["Fillo %i do pai %i, do avó %i" % (fillo, pai, avo), fillo])

        vista = Gtk.TreeView (modelo)
        tvcColumna = Gtk.TreeViewColumn ("Parentesco")
        celda = Gtk.CellRendererText()
        tvcColumna.pack_start(celda, True)
        tvcColumna.add_attribute (celda, "text", 0)
        vista.append_column (tvcColumna)

        tvcColumna2 = Gtk.TreeViewColumn ("Orde")
        celda2 = Gtk.CellRendererText()
        tvcColumna2.pack_start(celda2, True)
        tvcColumna2.add_attribute (celda2, "text", 1)
        vista.append_column(tvcColumna2)


        self.add (vista)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    ExemploGtkTreeViewArbore ()
    Gtk.main()
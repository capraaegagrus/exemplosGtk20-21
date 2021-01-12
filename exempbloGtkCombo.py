import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk

class ExemploGtkComboBox (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.ComboBox")
        self.set_size_request (200, 100)

        #Obxecto modelo
        lstNomes = Gtk.ListStore (int, str)
        lstNomes.append ( [16, "Juan"])
        lstNomes.append ([11, "Roberto"])
        lstNomes.append ([5, "Ana"])
        lstNomes.append ([18, "Rosa"])
        lstNomes.append ([21, "Xiana"])

        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL)

        cmbNomes = Gtk.ComboBox.new_with_model_and_entry(lstNomes)
        cmbNomes.connect ("changed", self.on_cmbNomes_changed)
        cmbNomes.set_entry_text_column (1)
        caixaV.pack_start (cmbNomes, False, False,0)

        self.add (caixaV)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def on_cmbNomes_changed (self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            edade, nome = modelo [fila][:2]
            print ("Seleccionado: edade=%d, nome=%s" % (edade, nome))
        else:
            txtNome = combo.get_child()
            print ("Escrito: %s" % txtNome.get_text())



if __name__ == "__main__":
    ExemploGtkComboBox ()
    Gtk.main()
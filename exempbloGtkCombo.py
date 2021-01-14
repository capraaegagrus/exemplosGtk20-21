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

        txtNomes = cmbNomes.get_child()
        txtNomes.connect ("activate", self.on_txtNomes_activated, lstNomes, cmbNomes)

        modelo_froitas = Gtk.ListStore (str)
        froitas = ["Mazán",
                   "Pera",
                   "Ameixa",
                   "Cereixa",
                   "Uva",
                   "Melón",
                   "Kiwi"]
        for froita in froitas:
            modelo_froitas.append ([froita])

        cmbFroitas = Gtk.ComboBox.new_with_model(modelo_froitas)
        cmbFroitas.connect ("changed", self.on_cmbFroitas_changed)
        renderer_text = Gtk.CellRendererText()
        cmbFroitas.pack_start(renderer_text, True)
        cmbFroitas.add_attribute (renderer_text, "text", 0)
        caixaV.pack_start (cmbFroitas, False, False, True)




        self.add (caixaV)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def on_cmbNomes_changed (self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            edade, nome = modelo [fila][:2]
            print ("Seleccionado: edade=%d, nome=%s" % (edade, nome))
            print (combo.get_active_id())
        else:
            txtNome = combo.get_child()
            print ("Escrito: %s" % txtNome.get_text())

    def on_txtNomes_activated (self, control, listaNomes, combo):
        nome = control.get_text()
        listaNomes.append ([99,nome])
        control.set_text("")
        indice = 0
        for nomeUsuario in listaNomes:
            print (nomeUsuario)
            if nomeUsuario[1] == nome:
                combo.set_active(indice)
            indice = indice + 1

    def on_cmbFroitas_changed (self, combo):
        #fila = combo.get_active_iter()
        fila = combo.get_active()
        if fila != -1:
            modelo = combo.get_model()
            froita = modelo [fila][0]
            print ("A froita elíxida é: %s" % froita)





if __name__ == "__main__":
    ExemploGtkComboBox ()
    Gtk.main()
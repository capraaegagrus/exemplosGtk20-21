import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk



class ExemploGtkTreeViewToogle (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.TreeView")
        self.set_size_request (250, 100)

        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing = 4)

        #Obxecto modelo
        modelo = Gtk.ListStore (str, bool)
        modelo.append (["Ethernet", True])
        modelo.append(["Wireless", True])
        modelo.append(["Bluetooth", False])
        modelo.append(["3g Mobíl", True])
        modelo.set_sort_func(0, self.ordear, None)

        trvComunicacion = Gtk.TreeView (modelo)
        caixaV.pack_start(trvComunicacion, True, True, 0)

        cellRendererText = Gtk.CellRendererText()
        cellRendererText.props.editable = True
        cellRendererText.connect ("edited", self.on_celdaTexto_edited, modelo)

        trcColumna = Gtk.TreeViewColumn  ("Tipo conexión")
        trcColumna.pack_start (cellRendererText, False)
        trcColumna.add_attribute(cellRendererText, "text", 0)
        trvComunicacion.append_column(trcColumna)
        trcColumna.set_sort_column_id(0)

        cellRendererToggle = Gtk.CellRendererToggle ()
        cellRendererToggle.connect ("toggled", self.on_celda_toggled, modelo)

        trcColumna = Gtk.TreeViewColumn ("Estado")
        trcColumna.pack_start (cellRendererToggle, False)
        trcColumna.add_attribute(cellRendererToggle, "active",1)
        trvComunicacion.append_column(trcColumna)

        caixaH1 = Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL, spacing = 4)
        lblTipo = Gtk.Label (label="Tipo")
        self.txtTipo = Gtk.Entry ()
        #chkEstado = Gtk.CheckButton.new_with_label(label="Estado")
        self.chkEstado = Gtk.CheckButton()
        self.chkEstado.set_label(("Estado"))
        caixaH1.pack_start(lblTipo, False, False, 0)
        caixaH1.pack_start(self.txtTipo, True, False, 0)
        caixaH1.pack_start(self.chkEstado, False, False, 0)
        caixaV.pack_start(caixaH1, True, True,0)

        caixaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        btnAceptar = Gtk.Button (label="Aceptar")
        btnAceptar.connect ("clicked", self.on_btnAceptar_clicked, modelo)
        btnCancelar = Gtk.Button(label="Cancelar")
        btnCancelar.connect("clicked", self.on_btnCancelar_clicked)
        btnEngadir = Gtk.Button(label = "Engadir")
        btnEngadir.connect("clicked", self.on_btnEngadir_clicked, modelo)
        caixaH2.pack_end(btnEngadir, False, False, 0)
        caixaH2.pack_end(btnCancelar, False, False, 0)
        caixaH2.pack_end(btnAceptar, False, False, 0)
        caixaV.pack_start(caixaH2, True, True, 0)

        self.add (caixaV)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def on_celda_toggled (self, celda, fila, modelo):
        modelo [fila][1] = not modelo [fila] [1]
        print ("O usuario fixo clic")

    def on_celdaTexto_edited (self, celda, fila, texto, modelo):
        modelo [fila][0] = texto

    def on_btnAceptar_clicked (self,boton, mod):
        if self.txtTipo.get_text()!= "":
            mod.append ([self.txtTipo.get_text(), self.chkEstado.get_active()])
            self.txtTipo.set_text("")
            self.chkEstado.set_active (False)

    def on_btnCancelar_clicked(self, boton):
        self.txtTipo.set_text("")
        self.chkEstado.set_active(False)

    def on_btnEngadir_clicked(self, boton, mod):
        mod.append(["", False])

    def ordear (self,modelo, fila1, fila2, datos):
        columna, _ = modelo.get_sort_column_id()
        if modelo.get_value (fila1,columna) < modelo.get_value (fila2, columna):
            return -1
        elif modelo.get_value (fila1,columna) == modelo.get_value (fila2, columna):
            return 0
        else:
            return 1



if __name__ == "__main__":
    ExemploGtkTreeViewToogle ()
    Gtk.main()
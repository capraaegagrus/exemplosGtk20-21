import sqlite3 as dbapi

import gi
gi.require_version ("Gtk", "3.0")

from gi.repository import Gtk



class ExemploGtkTreeViewBdFiltrado (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__ (self, title = "Exemplo con Gtk.TreeView con base de datos e filtrado")
        self.set_size_request (250, 100)

        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing = 4)

        #Obxecto modelo
        modelo = Gtk.ListStore (str,str,str,int,str)
        try:
            bbdd = dbapi.connect("baseDatosTreeView.dat")
        except dbapi.StandardError as e:
            print(e)
        else:
            print("Base de datos aberta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("select * from usuarios")

            for fila in cursor.fetchall():
                modelo.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
        else:
            print("Consulta executada")
        finally:
            cursor.close()
            bbdd.close()

        self.filtrado_sexo = "None"
        filtro_usuarios = modelo.filter_new()
        filtro_usuarios.set_visible_func (self.filtro_usuarios_sexo)

        trvDatosUsuarios = Gtk.TreeView(model = filtro_usuarios)
        seleccion = trvDatosUsuarios.get_selection()
        seleccion.connect("changed",self.on_trvDatosUsuarios_selection_changed)


        for i, tituloColumna in enumerate (["Dni", "Nome", "Direccion","Edade"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn (tituloColumna, celda, text=i)
            celda.props.editable = True
            celda.connect("edited", self.on_celda_edited, i, modelo)
            trvDatosUsuarios.append_column(columna)


        modeloCombo = Gtk.ListStore(str)
        modeloCombo.append (("Home",))
        modeloCombo.append (("Muller",))
        celda = Gtk.CellRendererCombo()
        celda.set_property("editable", True)
        celda.set_property("model", modeloCombo)
        celda.set_property ("text-column",0)
        celda.set_property ("has-entry", False)
        columna = Gtk.TreeViewColumn ("Combo", celda, text=4)
        celda.connect ("edited", self.on_celda_changed, modelo, 4)
        trvDatosUsuarios.append_column(columna)



        caixaV.pack_start(trvDatosUsuarios,True,True, 0)

        caixaH = Gtk.Box (orientation=Gtk.Orientation.HORIZONTAL, spacing =4)
        self.chkHome = Gtk.CheckButton(label ="Home")
        self.chkHome.connect ("toggled", self.on_chkXenero_toggled, filtro_usuarios)
        self.chkMuller = Gtk.CheckButton (label = "Muller")
        self.chkMuller.connect ("toggled", self.on_chkXenero_toggled, filtro_usuarios)
        caixaH.pack_start(self.chkHome, False, False, 2)
        caixaH.pack_start (self.chkMuller, False, False, 2)
        caixaV.pack_start (caixaH, True, True, 0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        self.txtDni = Gtk.Entry ()
        self.txtNome = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtEdade = Gtk.Entry()
        self.cmbSexo = Gtk.ComboBoxText()
        self.cmbSexo.append_text ("Home")
        self.cmbSexo.append_text ("Muller")
        caixaH.pack_start(self.txtDni, True, False, 2)
        caixaH.pack_start(self.txtNome, True, False, 2)
        caixaH.pack_start(self.txtDireccion, True, False, 2)
        caixaH.pack_start(self.txtEdade, True, False, 2)
        caixaH.pack_start(self.cmbSexo, True, False, 2)
        caixaV.pack_start (caixaH,True, True, 0)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        btnModificar = Gtk.Button (label = "Modificar")
        btnModificar.connect ("clicked", self.on_btnModificar_clicked, seleccion)
        caixaH.pack_end(btnModificar, False, False, 2)
        btnEngadir = Gtk.Button (label = "Engadir")
        btnEngadir.connect ("clicked", self.on_btnEngadir_clicked, modelo)
        caixaH.pack_end(btnEngadir, False, False, 2)
        caixaV.pack_end(caixaH, False, False, 2)

        self.add (caixaV)

        self.connect ("delete-event", Gtk.main_quit)
        self.show_all()

    def filtro_usuarios_sexo (self, modelo, fila, datos):
        if (self.filtrado_sexo is None or self.filtrado_sexo == "None"):
            return True
        else:
            return modelo [fila][4] == self.filtrado_sexo

    def on_chkXenero_toggled (self, control, modelo):
        if self.chkMuller.get_active() and self.chkHome.get_active()== False:
            self.filtrado_sexo = "Muller"
        elif self.chkMuller.get_active()== False and self.chkHome.get_active():
            self.filtrado_sexo = "Home"
        else:
            self.filtrado_sexo = "None"
        modelo.refilter()

    def on_celda_edited (self, celda, fila, texto, columna, modelo):
        modelo [fila][columna] = texto

    def on_celda_changed(self, combo, fila, texto, modelo, columna):
        modelo [fila][columna] = texto

    def on_trvDatosUsuarios_selection_changed(self, selection):
        modelo, fila = selection.get_selected()
        if fila  is not None:
            self.txtDni.set_text(modelo [fila][0])
            self.txtNome.set_text(modelo[fila][1])
            self.txtDireccion.set_text(modelo [fila][2])
            self.txtEdade.set_text (str(modelo [fila][3]))
            for i,elemento in enumerate (self.cmbSexo.get_model()):
                if elemento[0] == modelo [fila][4]:
                    self.cmbSexo.set_active(i)

    def on_btnModificar_clicked(self, boton, seleccion):
        modelo, fila = seleccion.get_selected()
        if fila  is not None:
            modelo [fila][0] = self.txtDni.get_text()
            modelo [fila][1] = self.txtNome.get_text()
            modelo[fila][2] = self.txtDireccion.get_text()
            modelo [fila][3] = int(self.txtEdade.get_text())
            modelo [fila][4] = self.cmbSexo.get_active_text()

            try:
                bbdd = dbapi.connect("baseDatosTreeView.dat")
            except dbapi.StandardError as e:
                print(e)
            else:
                print("Base de datos aberta")
            try:
                cursor = bbdd.cursor()
                cursor.execute("UPDATE usuarios SET nome=?, direccion=?, edade=?, sexo=? WHERE dni=?", (modelo [fila][1],
                                                                                                        modelo [fila][2],
                                                                                                        modelo [fila][3],
                                                                                                        modelo [fila][4],
                                                                                                        modelo [fila][0]))
                bbdd.commit()

            except dbapi.DatabaseError as e:
                print("Erro facendo a consulta: " + str(e))
            else:
                print("Consulta executada")
            finally:
                cursor.close()
                bbdd.close()

            self.txtDni.set_text("")
            self.txtNome.set_text("")
            self.txtDireccion.set_text("")
            self.txtEdade.set_text("")

    def on_btnEngadir_clicked (self, boton, modelo):
        rexistro =  (self.txtDni.get_text(),
                          self.txtNome.get_text(),
                          self.txtDireccion.get_text(),
                          int(self.txtEdade.get_text()),
                          self.cmbSexo.get_active_text())
        modelo.append(rexistro)

        try:
            bbdd = dbapi.connect("baseDatosTreeView.dat")
        except dbapi.StandardError as e:
            print(e)
        else:
            print("Base de datos aberta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("INSERT INTO usuarios VALUES (?,?,?,?,?)", (rexistro))
            bbdd.commit()

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
        else:
            print("Consulta executada")
        finally:
            cursor.close()
            bbdd.close()

        self.txtDni.set_text("")
        self.txtNome.set_text("")
        self.txtDireccion.set_text("")
        self.txtEdade.set_text("")

if __name__ == "__main__":
    ExemploGtkTreeViewBdFiltrado ()
    Gtk.main()
























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


        for i, tituloColumna in enumerate (["Dni", "Nome", "Direccion","Edade","Sexo"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn (tituloColumna, celda, text=i)
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





if __name__ == "__main__":
    ExemploGtkTreeViewBdFiltrado ()
    Gtk.main()
























#print (dbapi.apilevel)
#print (dbapi.threadsafety)
#print (dbapi.paramstyle)

try:
    bbdd = dbapi.connect ("baseDatos.dat")
    print (bbdd)


except dbapi.StandardError as e:
    print (e)
else:
    print ("Base de datos aberta")


try:
    cursor = bbdd.cursor ()
    print (cursor)

except dbapi.Error as e:
    print (e)
else:
    print ("Cursor preparado")



#try:
    #cursor.execute (""" create table usuarios (dni text,
     #                                          nome text,
      #                                         direccion text)""")

    #cursor.execute ("""insert into usuarios
     #                 values ('3333-A', 'Maria', 'Canceleiro')""")
    #cursor.execute ("""insert into usuarios
     #                  values ('4444-B', 'Manuel', 'Rosalia')""")
    #cursor.execute ("""insert into usuarios
     #                  values ('5555-C', 'Ana', 'Areal')""")
    #bbdd.commit()

#except dbapi.DatabaseError as e:
#    print ("Erro insertando os datos: " + str(e))
#else:
 #   print ("Base de datos creada")
  #  bbdd.close()


try:
    cursor.execute ("select * from usuarios")

    #fetchone a seguinte tupla
    #fetchall devolta un obxecto iterable con todalas tuplas
    #fetcmany numero de tuplas pasado por parametro

    for fila in cursor.fetchall():
        #print (fila)
        print ( "Nome: "+ fila [1])
        print ( "DNI: " + fila [0])
        print ( "Direccion: " + fila[2])

except dbapi.DatabaseError as e:
    print("Erro facendo a consulta: " + str(e))
else:
    print("Consulta executada")


dni = input ("Introduce o dni")

try:
    consulta = "select * from usuarios where dni = ?"
    print (consulta)
    cursor.execute(consulta, (dni,))
    for rexistro in cursor.fetchall():
        print (rexistro)

except dbapi.DatabaseError as e:
    print("Erro facendo a consulta: " + str(e))
else:
    print("Consulta executada")
finally:
    cursor.close()
    bbdd.close()
import sqlite3 as dbapi


#print (dbapi.apilevel)
#print (dbapi.threadsafety)
#print (dbapi.paramstyle)

try:
    bbdd = dbapi.connect ("baseDatosTreeView.dat")
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



try:
   cursor.execute (""" create table usuarios (dni text,
                                             nome text,
                                            direccion text,
                                            edade int,
                                            sexo text)""")

   cursor.execute ("""insert into usuarios
                     values ('3333-A', 'Maria', 'Canceleiro', 19, 'Muller')""")
   cursor.execute ("""insert into usuarios
                      values ('4444-B', 'Manuel', 'Rosalia', 34, 'Home')""")
   cursor.execute ("""insert into usuarios
                      values ('5555-C', 'Ana', 'Areal', 17, 'Muller')""")
   bbdd.commit()

except dbapi.DatabaseError as e:
    print ("Erro insertando os datos: " + str(e))
else:
    print ("Base de datos creada")

finally:
    cursor.close()
    bbdd.close()

"""
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
"""

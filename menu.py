from os import system
import pymysql

def InsertBD(cadena):
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="pwdmn"
    )
    cursor = conexion.cursor()
    cursor.execute(cadena)
    conexion.commit()

def selectBD(cadena):
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="pwdmn"
    )
    cursor = conexion.cursor()
    cursor.execute(cadena)

    return cursor.fetchall()

def agregar():
    print("¿Es una página nueva?")
    opcion = input("S/n  ")
    if opcion.lower() == "s":
        print("Ingresa la direccion de la pagina")
        sitio = input("-> ")
        print("Ingresa un alias")
        alias = input("-> ")
        sql = "INSERT INTO web (direccion, alias) VALUES ('{}', '{}');".format(sitio, alias)
        try:
            InsertBD(sql)
        except:
            print("Error de SQL")
            input()
    else:
        sql = "SELECT alias FROM web"
        resultados = selectBD(sql)
        print(resultados)
        input()


def menuPrincipal():
    system("clear")
    print("Selecciona una opcion")
    print("1.- Agregar contraseña")
    print("2.- Consultar contraseña")
    print("3.- Configuraciones")
    print("4.- Salir")
    opcion = int(input("-> "))
    return opcion

def seleccionPrincipal():
    continuar = True
    while continuar:
        selec = menuPrincipal()
        
        if selec == 1:
            agregar()
        elif selec == 2:
            pass #consultar
        elif selec == 3:
            pass #configuraciones
        elif selec == 4:
            print("bye")
            continuar = False
        else:
            print("ño")


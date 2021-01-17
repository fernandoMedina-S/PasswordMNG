#Libreria para conectar MySQL
import pymysql
from os import system
import sys
from pynput import keyboard as kb


#Cadena de conexion
conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        db="pwdmn"
    )

cursor = conexion.cursor()



def agregar():
    print("¿Es una página nueva?")
    opcion = input("S/n")
    if opcion.lower() == "s":
        print("Ingresa la direccion de la pagina")
        sitio = input("-> ")
    else:
        pass #Desplegar lista de sitios
    menu()
    

def menu():
    opcion = 1
    system("clear")
    print("Selecciona una opcion")
    print("1.- Agregar contraseña")
    print("2.- Consultar contraseña")
    print("3.- Configuraciones")
    print("4.- Salir")
    
    


menu()


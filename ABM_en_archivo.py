
from Clases import *
import os

def Hardcodear():
    persona = Usuario(29682301, "Franco", "Villafane", "06/11/1982")
    Grabar(persona)
    persona = Usuario(35924795, "Amelia", "Gomez", "04/04/1992")
    Grabar(persona)
    persona = Usuario(29873848, "Marcos", "Moneta", "23/12/1982")
    Grabar(persona)
    persona = Usuario(34989828, "Agostina", "Casella", "06/11/1982")
    Grabar(persona)
    persona = Usuario(39787343, "Milagos", "Chenda", "06/11/1982")
    Grabar(persona)
 
def Grabar(persona):
    if Verificar(persona):
        ordenar(persona)
    else:
        print("La persona ya existe en la base de datos.")

def Verificar(persona):
    si_no = True
    try:
        verif = open("abm.dat","r")
        for lines in verif:
            if persona.ID == int(lines.split(",")[0]):
                si_no = False
        return si_no
    finally:
        return si_no
        
def ordenar(persona):
    try:
        pasar = True
        ultimo = True
        ordenar = open("abm.dat","r")
        if ordenar:
            for lines in ordenar:
                
                if persona.ID < int(lines.split(",")[0]):
                    aux = open("auxi.dat","at")
                    pers = Usuario(lines.split(",")[0],lines.split(",")[1],lines.split(",")[2],lines.split(",")[3])
                    aux.write(f"{pers.ID},{pers.Nombre},{pers.Apellido},{pers.FechaNacimiento},\n")
                    aux.close()
                else:
                    aux = open("auxi.dat","at")
                    if pasar:
                        aux.write(f"{persona.ID},{persona.Nombre},{persona.Apellido},{persona.FechaNacimiento},\n")
                        pasar = False
                        ultimo = False
                    pers = Usuario(lines.split(",")[0],lines.split(",")[1],lines.split(",")[2],lines.split(",")[3])
                    aux.write(f"{pers.ID},{pers.Nombre},{pers.Apellido},{pers.FechaNacimiento},\n")
                    aux.close()
        if ultimo:
             aux = open("auxi.dat","at")
             aux.write(f"{persona.ID},{persona.Nombre},{persona.Apellido},{persona.FechaNacimiento},\n")
             aux.close()
             pasar = False
        ordenar.close()
        os.remove("abm.dat")
        ordenar = os.rename("auxi.dat","abm.dat")
    except:
        grabar = open("abm.dat", "at")
        grabar.write(f"{persona.ID},{persona.Nombre},{persona.Apellido},{persona.FechaNacimiento},\n")
        grabar.close()



def Leer():
    leer = open("abm.dat","r")
    try:
        for lines in leer:
            armapersona = lines.split(",")
            persona = Usuario(armapersona[0],armapersona[1],armapersona[2],armapersona[3])
            print(persona)
    finally:
        leer.close()

def MenuPrincipal():
    Leer()
    print("Ingrese DNI: ")
    DNI = int(input())
    print("Ingrese Nombre: ")
    nombre = input()
    print ("Ingrese Apellido: ")
    apellido = input()
    print ("Ingrese Fecha de Nacimiento: ")
    FechaNac = input()
    Nuevo = Usuario(DNI, nombre, apellido, FechaNac)
    Grabar(Nuevo)
    Leer()
Hardcodear()
MenuPrincipal()


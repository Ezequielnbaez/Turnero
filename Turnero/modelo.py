import sqlite3
import re
import tkinter
import logging
from tkinter import messagebox
from observador import Tema

logging.basicConfig(filename="log_dec.txt", level=logging.DEBUG,format="%(asctime)s %(message)s")
logging.basicConfig(level=logging.DEBUG)


class Database():
    def __init__(self): 
        self.crear_tabla_sqlite3()

    def conexion_sqlite3(self,):
        con = sqlite3.connect("turnero.db")
        return con

    def crear_tabla_sqlite3(self,):
        try:
            con = self.conexion_sqlite3()
            cursor = con.cursor()
            sqlite_tabla_usuarios = "CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY,dni integer UNIQUE, nroasociado integer, nombre text, apellido text, mail text, sexo integer, zona text)"
            cursor.execute(sqlite_tabla_usuarios)
            con.commit()
            print("Tabla de usuarios creada")

            sqlite_tabla_turnos ="CREATE TABLE IF NOT EXISTS turnos(id integer PRIMARY KEY, os integer, dnit integer UNIQUE, especializacion text, medicodni integer, fecha date)"
            cursor.execute(sqlite_tabla_turnos)
            con.commit()
            print("Tabla de turnos creada")

        except sqlite3.Error as error:
            print("Error creando la tabla", error)



    def alta_sqlite3(self,):
        sql="INSERT INTO usuarios(dni, nroasociado, nombre, apellido, mail, sexo, zona) VALUES(?, ?, ?, ?, ?, ?, ?)"
        return sql
 
#### DECORADOR ####

def dec_log_funciones(func):

    def envoltura(*args, **kwargs):
            logging.debug("Funcion: "+str(func.__name__))
            logging.debug("Argumentos: "+str(args)+ str(", ".join(f"{key}={value}" for key, value in kwargs.items())))

            return func(*args, **kwargs)
    return envoltura

 
#### ALTA-BAJA-MODIFICACION-USUARIO ####
class ABMU(Tema):
    def __init__(self):
        self.estado = None
        super().__init__()
    def set_estado(self, value):
        self.estado = value
        self.notificar()
    def get_estado(self):
        return self.estado 

    
    @dec_log_funciones
    def crear_usuario(self,datausuario):
        self.set_estado(1)
       #SQL
        try:
            mibase = sqlite3.connect('turnero.db')
            micursor = mibase.cursor()
            datos = (datausuario[0], datausuario[1], datausuario[2], datausuario[3], datausuario[4],datausuario[5], datausuario[6])
            sql = "INSERT INTO usuarios(dni, nroasociado, nombre, apellido, mail, sexo, zona) VALUES(?, ?, ?, ?, ?, ?, ?)"

            micursor.execute(sql,datos)
            mibase.commit()
            messagebox.showinfo(message="Usuario registrado", title="Registro")

        except:
            return "Ya existe alguien con ese DNI"
        
    @dec_log_funciones
    def modificar_usuario(self,datausuario,label_Warnings):
            mibase = sqlite3.connect('turnero.db')
            micursor = mibase.cursor()
            
            sql = "UPDATE usuarios SET nombre='"+str(datausuario[2])+"', apellido='"+datausuario[3]+"', mail='"+datausuario[4]+"' WHERE nroasociado="+datausuario[1]
            datos = (datausuario[0], datausuario[2], datausuario[3], datausuario[4], datausuario[1])
            micursor.execute(sql)
            mibase.commit()
            messagebox.showinfo(message="Usuario actualizado", title="Modificar")

            label_Warnings.configure(text = "Ya existe alguien con ese DNI")
    

    #### GENERAR NuMERO DE AFILIADO ####
    def generarNroAfiliado(self,optionMenu_zona,entry_Dni):
              if optionMenu_zona.get()=="CABA":
                  return 1+int(entry_Dni.get())
              elif optionMenu_zona.get()=="Mendoza" :
                  return 2+int(entry_Dni.get())
              elif optionMenu_zona.get()=="Cordoba":
                  return 3+int(entry_Dni.get())

    #### ASIGNAR SEXO A UN NuMERO ####
    def asignarSexo(self,combobox_sexo):
        if combobox_sexo.get()=="Masculino":
          return 1
        elif combobox_sexo.get()=="Femenino":
          return 0
        else:
          return 3

    #### CHEQUEO DE DATOS BIEN INGRESADOS ####
    def check_datos(self,label_Warnings,entry_Nombre,entry_Mail,entry_Dni,entry_Apellido,entry_confMail,optionMenu_zona,combobox_sexo,func,label_nroAsociado,button_acepMod):
     
        # Modificar
         if func=="MODIFICAR":
              label_Warnings.configure(text = "")
              if entry_Nombre.get()=="" or entry_Apellido.get()=="":
                  label_Warnings.configure(text = "Falta Nombre y Apellido")
              elif not entry_Nombre.get().isalnum() and not entry_Apellido.text.isalnum():
                  label_Warnings.configure(text = "Nombre y Apellido deben ser alfanumericos")
              elif not entry_Dni.get().isdigit():
                  label_Warnings.configure(text = "DNI debe ser numerico")
              elif entry_Mail.get()=="":
                  label_Warnings.configure(text = "Falta mail")
              else:
                   datausuario=(int(entry_Dni.get()), label_nroAsociado.cget("text"), str(entry_Nombre.get()), str(entry_Apellido.get()), str(entry_Mail.get()), None, None)
                   self.modificar_usuario(datausuario,label_Warnings)
                   entry_Nombre.configure(state="readonly")
                   entry_Apellido.configure(state="readonly")
                   entry_Dni.configure(state="readonly")
                   entry_Mail.configure(state="readonly")
                   button_acepMod.destroy()

        # Crear
         else:

              if entry_Nombre.get()=="" or entry_Apellido.get()=="":
                  return "Falta Nombre y Apellido"
              elif not re.match('[a-zA-Z]', entry_Nombre.get()) or not re.match('[a-zA-Z]', entry_Apellido.get()):
                  return "Nombre y Apellido deben ser solo letras"
              elif entry_Mail.get()!=entry_confMail.get():
                  return "Los mails no estan bien ingresados"
              elif not entry_Dni.get().isdigit():
                  return "DNI debe ser numerico"
              elif entry_Mail.get()=="":
                  return "Falta mail"
              else:
                   self.datausuario=(int(entry_Dni.get()),self.generarNroAfiliado(optionMenu_zona,entry_Dni), str(entry_Nombre.get()), str(entry_Apellido.get()), str(entry_Mail.get()), self.asignarSexo(combobox_sexo), str(optionMenu_zona.get()))
                   self.crear_usuario(self.datausuario)




#### ALTA-BAJA-MODIFICACION-TURNO ####
class ABMT():
    def check_turn(self):
            date=self.cal.get_date()+" 00:00:00"
            dataturno=(str(self.optionMenu_conven.get()), str(self.entry_Dni.get()), str(self.combobox_spec.get()), 11111, self.datetime.strptime(date, '%m/%d/%y %H:%M:%S'))
            self.crear_turno(dataturno)
            self.label_fecha.configure(text="Turno para el "+str(dataturno[4]))

    def crear_turno(datos,self):
                try:
                    mibase = sqlite3.connect('turnero.db')
                    micursor = mibase.cursor()
                    sql = "INSERT INTO turnos (os, dnit, especializacion, medicodni, fecha) VALUES (?, ?, ?, ?, ?)"
                    datos = (datos[0], datos[1], datos[2], datos[3], datos[4])
                    micursor.execute(sql, datos)
                    mibase.commit()
                    self.label_Warnings.configure(text = "Turno agregado")
                except:
                    print("Error")

class BSE():
    def __init__(self,entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf,button_acepMod):
        super().__init__()
        self.entry_Nombre= entry_Nombre
        self.entry_Apellido= entry_Apellido
        self.entry_Dni= entry_Dni
        self.entry_Mail= entry_Mail
        self.optionMenu_Zona= optionMenu_Zona
        self.label_nroAsociado= label_nroAsociado
        self.button_modificarAf= button_modificarAf
        self.button_acepMod = button_acepMod
    #### BUSCAR USUARIO EN BASE DE DATOS ####
    def buscar_usuario(self,entry_Bus,label_WarningB,tree):
            tree.delete(*tree.get_children())
            mibase = sqlite3.connect('turnero.db')
            micursor = mibase.cursor()
            numero=0
            if entry_Bus.get().isdigit():
                numero=entry_Bus.get()
            sql ="SELECT * FROM usuarios WHERE ? in (nombre, apellido, mail, zona) OR ? in (dni, nroasociado)"
            datos=[str(entry_Bus.get()),int(numero)]
            micursor.execute(sql,datos)
            miresult = micursor.fetchall()
            if miresult=="":
               label_WarningB.configure("No encontrado")
            else:
                for dt in miresult: 
                    tree.insert("", tkinter.END, values =(dt[1],dt[2],dt[3],dt[4],dt[5],dt[7]))
                    print(dt)
    #### SELECCIONAR USUARIO BUSCADO ####
    def seleccionar_usuario(self,tree,label_Warnings):
        self.entry_Nombre.configure(state="normal")
        self.entry_Apellido.configure(state="normal")
        self.entry_Dni.configure(state="normal")
        self.entry_Mail.configure(state="normal")

        self.entry_Nombre.delete(0, 'end')

        self.entry_Apellido.delete(0, 'end')

        self.entry_Mail.delete(0, 'end')

        self.entry_Dni.delete(0, 'end')



        try:
            curItem = tree.focus()
            datos=tree.item(curItem, "values")
            self.entry_Dni.insert(0,datos[0])
            self.label_nroAsociado.configure(text=datos[1])
            self.entry_Nombre.insert(0,datos[2])
            self.entry_Apellido.insert(0,datos[3])
            self.entry_Mail.insert(0,datos[4])
            self.optionMenu_Zona.set(datos[5])
            self.button_modificarAf.configure(state="normal")
            self.button_acepMod.configure(state="normal")

            self.entry_Nombre.configure(state="disabled")
            self.entry_Apellido.configure(state="disabled")
            self.entry_Dni.configure(state="disabled")
            self.entry_Mail.configure(state="disabled")
            messagebox.showinfo(message="Usuario seleccionado", title="Aviso")

            return ""
        except:
            return "No hay nada seleccionado"
 
    @dec_log_funciones
    def eliminar_usuario(self,tree,label_WarningsB):
        respuesta=messagebox.askquestion(message="Desea eliminar este usuario", title="Eliminar usuario")
        if respuesta=="yes":
            try:
                curItem = tree.focus()
                datos=tree.item(curItem, "values")
                tree.delete(curItem)
                mibase = sqlite3.connect('turnero.db')
                micursor = mibase.cursor()
                sql ="DELETE FROM usuarios WHERE nroasociado="+datos[1]
                micursor.execute(sql)
                mibase.commit()
          
            except:
                label_WarningsB.configure(text="No hay nada seleccionado")
        else:
            return

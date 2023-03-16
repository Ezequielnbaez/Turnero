import tkinter
import tkinter.messagebox
import customtkinter
import random
import mysql.connector

from datetime import datetime
from tkinter import *
from tkinter import font,ttk
from tkcalendar import Calendar
from tkinter import messagebox

customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")

mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="turnero")
micursor = mibase.cursor()

#========Funciones Ingresar Afiliado========= Dios me perdone por este código tan feo
def crearNroAfiliado(optionMenu_zona,entry_Dni):
          if optionMenu_zona.get()=="CABA":
              return 1+int(entry_Dni.get())
          elif optionMenu_zona.get()=="Mendoza" :
              return 2+int(entry_Dni.get())
          elif optionMenu_zona.get()=="Cordoba":
              return 3+int(entry_Dni.get())

def asignarSexo(combobox_sexo):
          if combobox_sexo.get()=="Masculino":
              return 1
          else:
              return 0

def check_datos(label_Warning,entry_Nombre,entry_Mail,entry_Dni,entry_Apellido,entry_confMail,optionMenu_zona,combobox_sexo,func,label_nroAsociado,button_acepMod):
          
     if func=="MODIFICAR":
          label_Warning.configure(text = "")
          if entry_Nombre.get()=="" or entry_Apellido.get()=="":
              label_Warning.configure(text = "Falta Nombre y Apellido")
          elif not entry_Nombre.get().isalnum() and not entry_Apellido.text.isalnum():
              label_Warning.configure(text = "Nombre y Apellido deben ser alfanuméricos")
          elif not entry_Dni.get().isdigit():
              label_Warning.configure(text = "DNI debe ser numérico")
          elif entry_Mail.get()=="":
              label_Warning.configure(text = "Falta mail")
          else:
               datausuario=(int(entry_Dni.get()), label_nroAsociado.text, str(entry_Nombre.get()), str(entry_Apellido.get()), str(entry_Mail.get()), None, None)
               updateUser(datausuario,label_Warning)
               entry_Nombre.configure(state="readonly")
               entry_Apellido.configure(state="readonly")
               entry_Dni.configure(state="readonly")
               entry_Mail.configure(state="readonly")
               button_acepMod.destroy()
     else:
          label_Warning.configure(text = "")
          if entry_Nombre.get()=="" or entry_Apellido.get()=="":
              label_Warning.configure(text = "Falta Nombre y Apellido")
          elif not entry_Nombre.get().isalnum() and not entry_Apellido.get().isalnum():
              label_Warning.configure(text = "Nombre y Apellido deben ser alfanuméricos")
          elif entry_Mail.get()!=entry_confMail.get():
              label_Warning.configure(text = "Los mails no están bien ingresados")
          elif not entry_Dni.get().isdigit():
              label_Warning.configure(text = "DNI debe ser numérico")
          elif entry_Mail.get()=="":
              label_Warning.configure(text = "Falta mail")
          else:
               datausuario=(int(entry_Dni.get()), crearNroAfiliado(optionMenu_zona,entry_Dni), str(entry_Nombre.get()), str(entry_Apellido.get()), str(entry_Mail.get()), asignarSexo(combobox_sexo), str(optionMenu_zona.get()))
               crear_usuario(datausuario,label_Warning)




def crear_usuario(datausuario,label_Warning):

      #SQL
        try:
            mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="turnero")
            micursor = mibase.cursor()
            sql = "INSERT INTO usuarios (dni, nroasociado, nombre, apellido, mail, sexo, zona) VALUES (%s, %s, %s,%s, %s, %s, %s)"
            datos = (datausuario[0], datausuario[1], datausuario[2], datausuario[3], datausuario[4],datausuario[5], datausuario[6])
            micursor.execute(sql, datos)
            mibase.commit()
            print(messagebox.showinfo(message="Usuario registrado", title="Registro"))
        except:
            label_Warning.configure(text = "Ya existe alguien con ese DNI")
        

#========Funciones main- Crear Turno========= Dios me perdone por este código tan feo
def updateUser(datausuario,label_Warning):
      #SQL

            mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="turnero")
            micursor = mibase.cursor()
            
            sql = "UPDATE usuarios SET nombre='"+str(datausuario[2])+"', apellido='"+datausuario[3]+"', mail='"+datausuario[4]+"' WHERE nroasociado="+datausuario[1]
            datos = (datausuario[0], datausuario[2], datausuario[3], datausuario[4], datausuario[1])
            micursor.execute(sql)
            mibase.commit()
            mibase.close()
            messagebox.showinfo(message="Usuario actualizado", title="Modificar")

            label_Warning.configure(text = "Ya existe alguien con ese DNI")

def buscar_nroAsc(label_nroAsociado):
        label_nroAsociado.configure(text = "20"+str(entry_Dni.get())+str(random.randrange(0, 25)))

def mostrarAfiliado(afiliado):
        print(afiliado)

def check_turn(label_Warning):
        label_Warning.configure(text = "")
        date=cal.get_date()+" 00:00:00"
        dataturno=(str(optionMenu_conven.get()), str(entry_Dni.get()), str(combobox_spec.get()), 11111, datetime.strptime(date, '%m/%d/%y %H:%M:%S'))
        crear_turno(dataturno)
        print(dataturno)

def crear_turno(datos):
            try:
                mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="turnero")
                micursor = mibase.cursor()
                sql = "INSERT INTO turnos (os, dnit, especializacion, medicodni, fecha) VALUES (%s, %s, %s,%s, %s)"
                datos = (datos[0], datos[1], datos[2], datos[3], datos[4])
                micursor.execute(sql, datos)
                mibase.commit()
                self.label_Warning.configure(text = "Turno agregado")
                mibase.close()
            except:
                print("An exception occurred")

#========Funciones buscarUsuario=========
def buscar(tree,entry_Bus,label_WarningB):
        tree.delete(*tree.get_children())
        mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="turnero")
        micursor = mibase.cursor()
        sql =("SELECT * FROM usuarios WHERE %s in (dni, nroasociado, nombre, apellido, mail, zona)")
        datos=[str(entry_Bus.get())]
        micursor.execute(sql, datos)
        miresult = micursor.fetchall()
        mibase.close()
        if miresult=="":
           label_WarningB.configure("No encontrado")
        else:
            for dt in miresult: 
                tree.insert("", tkinter.END, values =(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6]))

def seleccionar(buscarUsu,tree,entry_Nombre,entry_Apellido,entry_Dni,entry_Mail,optionMenu_Zona,label_nroAsociado,button_modificarAf,label_WarningB):
     
    try:
        curItem = tree.focus()
        datos=tree.item(curItem, "values")
        entry_Dni.insert(0,datos[0])
        label_nroAsociado.configure(text=datos[1])
        entry_Nombre.insert(0,datos[2])
        entry_Apellido.insert(0,datos[3])
        entry_Mail.insert(0,datos[4])
        optionMenu_Zona.set(datos[5])
        button_modificarAf.configure(state=NORMAL)

        entry_Nombre.configure(state="readonly")
        entry_Apellido.configure(state="readonly")
        entry_Dni.configure(state="readonly")
        entry_Mail.configure(state="readonly")
        buscarUsu.destroy()

    except:
        label_WarningB.configure(text="No hay nada seleccionado")
 
def eliminar(tree,label_WarningB,buscarUsu):
    respuesta=messagebox.askquestion(message="¿Desea eliminar este usuario?", title="Eliminar usuario")
    if respuesta=="yes":
        try:
            curItem = tree.focus()
            datos=tree.item(curItem, "values")
            tree.delete(curItem)
            mibase = mysql.connector.connect(host="localhost",user="root",passwd="",database="turnero")
            micursor = mibase.cursor()
            sql ="DELETE FROM usuarios WHERE nroasociado="+datos[1]
            micursor.execute(sql)
            mibase.commit()
            mibase.close()
        except:
            label_WarningB.configure(text="No hay nada seleccionado")
    else:
        return


def buscarUsuario(entry_Nombre,entry_Apellido,entry_Dni,entry_Mail,optionMenu_Zona,label_nroAsociado,button_modificarAf):

    #Frame
    buscarUsu = customtkinter.CTk()
    buscarUsu.title("Buscar afiliado")
    buscarUsu.geometry("620x220")
    buscarUsu.resizable(width=False, height=True)
    frame_formB = customtkinter.CTkFrame(master=buscarUsu, width=180, corner_radius=0)
    frame_formB.grid(row=0, column=0, sticky="nswe")

    frame_tree = customtkinter.CTkFrame(master=buscarUsu, width=180, corner_radius=0)
    frame_tree.grid(row=1, column=0, sticky="nswe")

    frame_formB.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    frame_formB.rowconfigure((0, 1, 2, 3, 4, 5), minsize=10)
    frame_formB.columnconfigure((0, 1, 2, 3), weight=1)
    frame_formB.columnconfigure((0, 1, 2, 3), minsize=10)

    #TreeView
    tree = ttk.Treeview(frame_tree, columns = (1,2,3,4,5,6), height = 10, show = "headings")
    tree.grid(row=1, column=0, columnspan=1, pady=0, padx=0, sticky="")

    tree.heading(1, text="Dni")
    tree.heading(2, text="NroAsociado")
    tree.heading(3, text="Nombre")
    tree.heading(4, text="Apellido")
    tree.heading(5, text="Mail")
    tree.heading(6, text="Zona")

    tree.column(1, width = 100)
    tree.column(2, width = 100)
    tree.column(3, width = 100)
    tree.column(4, width = 100)
    tree.column(5, width = 100)
    tree.column(6, width = 100)

    # Inserting Scrollbar
    scroll = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
    scroll.grid(row=1, column=1, columnspan=1, pady=5, padx=0, sticky="")

    tree.configure(yscrollcommand=scroll.set)
    #Datos

    label_Bus = customtkinter.CTkLabel(master=frame_formB, text="Datos: ", text_font=("Roboto Medium", -16))
    label_Bus.grid(row=2, column=0, columnspan=1, pady=5, padx=0, sticky="")
    entry_Bus = customtkinter.CTkEntry(master=frame_formB,text="Datos", placeholder_text="Datos")
    entry_Bus.grid(row=2, column=1, columnspan=1, pady=5, padx=5, sticky="")

    label_WarningB = customtkinter.CTkLabel(master=frame_formB, text="", text_font=("Roboto Medium", -10))
    label_WarningB.grid(row=3, column=1, columnspan=1, pady=5, padx=0, sticky="")
    button_buscarUs = customtkinter.CTkButton(master=frame_formB, text="Buscar", border_width=2, fg_color=None, command=lambda : buscar(tree,entry_Bus,label_WarningB))
    button_buscarUs.grid(row=2, column=3, pady=5, padx=5)
    button_seleccionarUs = customtkinter.CTkButton(master=frame_formB, text="Seleccionar", border_width=2, fg_color=None, command=lambda : seleccionar(buscarUsu,tree,entry_Nombre,entry_Apellido,entry_Dni,entry_Mail,optionMenu_Zona,label_nroAsociado,button_modificarAf,label_WarningB))
    button_seleccionarUs.grid(row=2, column=4, pady=5, padx=5)
    button_eliminar = customtkinter.CTkButton(master=frame_formB, text="Eliminar", border_width=2, fg_color=None, command=lambda : eliminar(tree,label_WarningB,buscarUsu))
    button_eliminar.grid(row=3, column=4, pady=5, padx=5)

    buscarUsu.mainloop()

def ingresarAfiliado():

      #Frame
      crearUsu = customtkinter.CTk()
      crearUsu.title("Crear usuario")
      crearUsu.geometry("610x220")  
      
      frame_form = customtkinter.CTkFrame(master=crearUsu,
                                                 width=180,
                                                 corner_radius=0)
      frame_form.grid(row=0, column=0, sticky="nswe")

      frame_form.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
      frame_form.rowconfigure((0, 1, 2, 3, 4, 5), minsize=10)
      frame_form.columnconfigure((0, 1, 2), weight=1)
      frame_form.columnconfigure((0, 1, 2), minsize=10)

      #Datos
      label_titlemed = customtkinter.CTkLabel(master=frame_form, text="Crear turno", text_font=("Roboto Medium", -20))
      label_titlemed.grid(row=0, column=1, pady=0, padx=10)

      label_Warning = customtkinter.CTkLabel(master=frame_form, text="", text_font=("Roboto Medium", -10))
      label_Warning.grid(row=5, column=1, columnspan=1, pady=5, padx=0, sticky="")

      label_Nombre = customtkinter.CTkLabel(master=frame_form, text="Nombre: ", text_font=("Roboto Medium", -16))
      label_Nombre.grid(row=1, column=0, columnspan=1, pady=5, padx=0, sticky="")

      label_Apellido = customtkinter.CTkLabel(master=frame_form, text="Apellido: ", text_font=("Roboto Medium", -16))
      label_Apellido.grid(row=1, column=2, columnspan=1, pady=5, padx=0, sticky="")

      entry_Nombre = customtkinter.CTkEntry(master=frame_form,text="Nombre", placeholder_text="Nombre")
      entry_Apellido = customtkinter.CTkEntry(master=frame_form,text="Apellido", placeholder_text="Apellido")

      entry_Nombre.grid(row=1, column=1, columnspan=1, pady=5, padx=5, sticky="")
      entry_Apellido.grid(row=1, column=3, columnspan=1, pady=5, padx=5, sticky="")

      label_Mail = customtkinter.CTkLabel(master=frame_form, text="Mail: ", text_font=("Roboto Medium", -16))
      label_Mail.grid(row=2, column=0, columnspan=1, pady=5, padx=0, sticky="")
      entry_Mail = customtkinter.CTkEntry(master=frame_form,text="Correo electr.", placeholder_text="Correo electrónico")
      entry_Mail.grid(row=2, column=1, columnspan=1, pady=5, padx=5, sticky="")

      label_confMail = customtkinter.CTkLabel(master=frame_form, text="Confirmar correo: ", text_font=("Roboto Medium", -16))
      label_confMail.grid(row=2, column=2, columnspan=1, pady=5, padx=0, sticky="")
      entry_confMail = customtkinter.CTkEntry(master=frame_form,text="", placeholder_text="Correo electrónico")
      entry_confMail.grid(row=2, column=3, columnspan=1, pady=5, padx=5, sticky="")

      label_sexo = customtkinter.CTkLabel(master=frame_form, text="Sexo: ", text_font=("Roboto Medium", -16))
      label_sexo.grid(row=3, column=0, columnspan=1, pady=5, padx=0, sticky="")
      combobox_sexo = customtkinter.CTkComboBox(master=frame_form,values=["Masculino","Femenino"])
      combobox_sexo.grid(row=3, column=1, columnspan=1, pady=10, padx=20, sticky="we")

      label_dni = customtkinter.CTkLabel(master=frame_form, text="Dni: ", text_font=("Roboto Medium", -16))
      label_dni.grid(row=4, column=0, columnspan=1, pady=5, padx=0, sticky="")
      entry_Dni = customtkinter.CTkEntry(master=frame_form,text="Dni", placeholder_text="Dni")
      entry_Dni.grid(row=4, column=1, columnspan=1, pady=5, padx=5, sticky="")

      label_zona = customtkinter.CTkLabel(master=frame_form, text="Zona: ", text_font=("Roboto Medium", -16))
      label_zona.grid(row=3, column=2, columnspan=1, pady=5, padx=0, sticky="")
      optionMenu_zona = customtkinter.CTkOptionMenu(master=frame_form, values=["CABA", "Mendoza", "Córdoba"])
      optionMenu_zona.set("CABA")
      optionMenu_zona.grid(row=3, column=3, columnspan=1, pady=5, padx=5, sticky="")

      button_crearUs = customtkinter.CTkButton(master=frame_form, text="Agregar", border_width=2, fg_color=None, command=lambda : check_datos(label_Warning,entry_Nombre,entry_Mail,entry_Dni,entry_Apellido,entry_confMail,optionMenu_zona,combobox_sexo,"CREAR",None, None))
      button_crearUs.grid(row=4, column=3, pady=5, padx=5)

      crearUsu.mainloop()



def main():
    
    #============Funciones============

    def modificarDatos():

        entry_Nombre.configure(state=NORMAL)
        entry_Apellido.configure(state=NORMAL)
        entry_Dni.configure(state=NORMAL)
        entry_Mail.configure(state=NORMAL)
            
        button_acepMod = customtkinter.CTkButton(master=frame_med, text="Aceptar modificación", border_width=2, fg_color=None, command=lambda: check_datos(label_Warning,entry_Nombre,entry_Mail,entry_Dni,entry_Apellido,None,optionMenu_Zona,None,"MODIFICAR",label_nroAsociado,button_acepMod))
        button_acepMod.grid(row=5, column=3, pady=5, padx=5)

        

    mainView = customtkinter.CTk()
    mainView.resizable(width=False, height=False)
    mainView.title("Buscar afiliado")
    mainView.geometry("1100x310")

    # ============ Creación de frames ============

    frame_izq = customtkinter.CTkFrame(master=mainView,
                                                 width=180,
                                                 corner_radius=0)
    frame_izq.grid(row=0, column=0, sticky="nswe")

    frame_med = customtkinter.CTkFrame(master=mainView)
    frame_med.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    frame_der = customtkinter.CTkFrame(master=mainView,
                                                 width=180,
                                                 corner_radius=0)
    frame_der.grid(row=0, column=3, sticky="nswe")

    # ============ frame_izq ============

    frame_izq.grid_rowconfigure(0, minsize=10)   
    frame_izq.grid_rowconfigure(5, weight=1)  
    frame_izq.grid_rowconfigure(8, minsize=20)    
    frame_izq.grid_rowconfigure(11, minsize=10) 

    label_titleIzq = customtkinter.CTkLabel(master=frame_izq,
                                              text="Calendario",
                                              text_font=("Roboto Medium", -20))
    label_titleIzq.grid(row=0, column=0, pady=0, padx=10)

    label_fecha = customtkinter.CTkLabel(master=frame_izq,
                                              text="",
                                              text_font=("Roboto Medium", -16))
    label_fecha.grid(row=1, column=0, pady=10, padx=10)


    cal = Calendar(master=frame_izq, selectmode = 'day', year = 2020, month = 5, day = 22)

    cal.grid(row=2, column=0, pady=10, padx=10)

    # ============ frame_med ============
    frame_med.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    frame_med.rowconfigure((0, 1, 2, 3, 4, 5), minsize=10)
    frame_med.columnconfigure((0, 1, 2), weight=1)
    frame_med.columnconfigure((0, 1, 2), minsize=10)

    label_titlemed = customtkinter.CTkLabel(master=frame_med, text="Crear turno", text_font=("Roboto Medium", -20))
    label_titlemed.grid(row=0, column=1, pady=0, padx=10)

    label_Nombre = customtkinter.CTkLabel(master=frame_med, text="Nombre: ", text_font=("Roboto Medium", -16))
    label_Nombre.grid(row=1, column=0, columnspan=1, pady=5, padx=0, sticky="")

    label_Apellido = customtkinter.CTkLabel(master=frame_med, text="Apellido: ", text_font=("Roboto Medium", -16))
    label_Apellido.grid(row=1, column=2, columnspan=1, pady=5, padx=0, sticky="")

    label_Mail = customtkinter.CTkLabel(master=frame_med, text="Mail: ", text_font=("Roboto Medium", -16))
    label_Mail.grid(row=2, column=0, columnspan=1, pady=5, padx=0, sticky="")

    label_Esp = customtkinter.CTkLabel(master=frame_med, text="Especialidad: ", text_font=("Roboto Medium", -16))
    label_Esp.grid(row=3, column=0, columnspan=1, pady=5, padx=0, sticky="")

    label_med = customtkinter.CTkLabel(master=frame_med, text="Medico: ", text_font=("Roboto Medium", -16))
    label_med.grid(row=2, column=2, columnspan=1, pady=5, padx=0, sticky="")

    label_dni = customtkinter.CTkLabel(master=frame_med, text="Dni: ", text_font=("Roboto Medium", -16))
    label_dni.grid(row=4, column=0, columnspan=1, pady=5, padx=0, sticky="")

    label_convenio = customtkinter.CTkLabel(master=frame_med, text="Convenio: ", text_font=("Roboto Medium", -16))
    label_convenio.grid(row=3, column=2, columnspan=1, pady=5, padx=0, sticky="")

    label_nroAsoc = customtkinter.CTkLabel(master=frame_med, text="Nro. Asociado: ", text_font=("Roboto Medium", -16))
    label_nroAsoc.grid(row=4, column=2, columnspan=1, pady=5, padx=0, sticky="")

    label_Warning = customtkinter.CTkLabel(master=frame_med, text="", text_font=("Roboto Medium", -10))
    label_Warning.grid(row=5, column=1, columnspan=1, pady=5, padx=0, sticky="")

    entry_Nombre = ttk.Entry(master=frame_med,text="",font=font.Font(family="Roboto Medium", size=10))
    entry_Apellido = ttk.Entry(master=frame_med,text="",font=font.Font(family="Roboto Medium", size=10))

    entry_Nombre.grid(row=1, column=1, columnspan=1, pady=5, padx=5, sticky="")
    entry_Apellido.grid(row=1, column=3, columnspan=1, pady=5, padx=5, sticky="")


    entry_Mail = ttk.Entry(master=frame_med,text="",font=font.Font(family="Roboto Medium", size=9))
    entry_Mail.grid(row=2, column=1, columnspan=1, pady=5, padx=5, sticky="")

    combobox_meds = customtkinter.CTkComboBox(master=frame_med,values=["Medico1","Medico2","Medico2"])
    combobox_meds.grid(row=2, column=3, columnspan=1, pady=10, padx=20, sticky="we")

    entry_Dni = ttk.Entry(master=frame_med,text="",font=font.Font(family="Roboto Medium", size=9))
    entry_Dni.grid(row=4, column=1, columnspan=1, pady=5, padx=5, sticky="")

    combobox_spec = customtkinter.CTkComboBox(master=frame_med,values=["Traumatología", "Otorrinolaringología", "Pediatría", "Cardiología", "Clínico"])
    combobox_spec.grid(row=3, column=1, columnspan=1, pady=10, padx=20, sticky="we")

    optionMenu_conven = customtkinter.CTkOptionMenu(master=frame_med, values=["conv1", "conv2", "conv3"])
    optionMenu_conven.set("conv1")
    optionMenu_conven.grid(row=3, column=3, columnspan=1, pady=5, padx=5, sticky="")

    label_nroAsociado = customtkinter.CTkLabel(master=frame_med, text="", text_font=("Roboto Medium", -15))
    label_nroAsociado.grid(row=4, column=3, columnspan=1, pady=5, padx=5, sticky="")

    label_zona = customtkinter.CTkLabel(master=frame_med, text="Zona", text_font=("Roboto Medium", -15))
    label_zona.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")

    optionMenu_Zona = customtkinter.CTkOptionMenu(master=frame_med, values=["CABA", "Córdoba", "Mendoza"])
    optionMenu_Zona.set("None")
    optionMenu_Zona.grid(row=5, column=1, columnspan=1, pady=5, padx=5, sticky="")

    button_crearTu = customtkinter.CTkButton(master=frame_med, text="Crear turno", border_width=2, fg_color=None, command=check_turn)
    button_crearTu.grid(row=5, column=3, pady=5, padx=5)

    # ============ frame_der ============
    button_crearAf = customtkinter.CTkButton(master=frame_der, text="Ingresar afiliado", border_width=2, fg_color=None, command=ingresarAfiliado)
    button_crearAf.grid(row=0, column=0, pady=5, padx=5)

    button_buscarAf = customtkinter.CTkButton(master=frame_der, text="Buscar afiliado", border_width=2, fg_color=None, command=lambda: buscarUsuario(entry_Nombre,entry_Apellido,entry_Dni,entry_Mail,optionMenu_Zona,label_nroAsociado,button_modificarAf))
    button_buscarAf.grid(row=1, column=0, pady=5, padx=5)

    button_modificarAf = customtkinter.CTkButton(master=frame_der, text="Modificar afiliado", border_width=2, fg_color=None, state=DISABLED, command=modificarDatos)
    button_modificarAf.grid(row=2, column=0, pady=5, padx=5)

    mainView.mainloop()
       
main()
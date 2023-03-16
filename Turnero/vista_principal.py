####LIBRERiAS####

import tkinter
import customtkinter
import sqlite3
import modelo
import controlador_principal
import controlador_ingresar

from datetime import datetime
from tkinter import *
from tkinter import font,ttk
from tkcalendar import Calendar

#### ESTILO DE TKINTER ####
customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")
        

class PanelPrincipal(customtkinter.CTk):
   def __init__(self): 
        self.modeldb = modelo.Database()
        self.controlador = controlador_principal.Controller(self.modeldb)
        self.controladorAlta = controlador_ingresar.Controller()
        super().__init__()
   
        # Generacion de vista
        self.resizable(width=False, height=False)
        self.title("Buscar afiliado")
        self.geometry("1100x310")

        # Configuracion de Frames
        self.frame_izq = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_izq.grid(row=0, column=0, sticky="nswe")

        self.frame_med = customtkinter.CTkFrame(master=self)
        self.frame_med.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_der = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_der.grid(row=0, column=3, sticky="nswe")

        # Frame izquierdo
        self.frame_izq.grid_rowconfigure(0, minsize=10)   
        self.frame_izq.grid_rowconfigure(5, weight=1)  
        self.frame_izq.grid_rowconfigure(8, minsize=20)    
        self.frame_izq.grid_rowconfigure(11, minsize=10) 

        self.label_titleIzq = customtkinter.CTkLabel(master=self.frame_izq,text="Calendario",font=("Roboto Medium", -20))
        self.label_titleIzq.grid(row=0, column=0, pady=0, padx=10)

        self.label_fecha = customtkinter.CTkLabel(master=self.frame_izq,text="",font=("Roboto Medium", -16))
        self.label_fecha.grid(row=1, column=0, pady=10, padx=10)

        self.cal = Calendar(master=self.frame_izq, selectmode = 'day', year = 2020, month = 5, day = 22)

        self.cal.grid(row=2, column=0, pady=10, padx=10)

        # Frame medio
        self.frame_med.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.frame_med.rowconfigure((0, 1, 2, 3, 4, 5), minsize=10)
        self.frame_med.columnconfigure((0, 1, 2), weight=1)
        self.frame_med.columnconfigure((0, 1, 2), minsize=10)

        self.label_titlemed = customtkinter.CTkLabel(master=self.frame_med, text="Crear turno", font=("Roboto Medium", -20))
        self.label_titlemed.grid(row=0, column=1, pady=0, padx=10)

        self.label_Nombre = customtkinter.CTkLabel(master=self.frame_med, text="Nombre: ", font=("Roboto Medium", -16))
        self.label_Nombre.grid(row=1, column=0, columnspan=1, pady=5, padx=0, sticky="")

        self.label_Apellido = customtkinter.CTkLabel(master=self.frame_med, text="Apellido: ", font=("Roboto Medium", -16))
        self.label_Apellido.grid(row=1, column=2, columnspan=1, pady=5, padx=0, sticky="")

        self.label_Mail = customtkinter.CTkLabel(master=self.frame_med, text="Mail: ", font=("Roboto Medium", -16))
        self.label_Mail.grid(row=2, column=0, columnspan=1, pady=5, padx=0, sticky="")

        self.label_Esp = customtkinter.CTkLabel(master=self.frame_med, text="Especialidad: ", font=("Roboto Medium", -16))
        self.label_Esp.grid(row=3, column=0, columnspan=1, pady=5, padx=0, sticky="")

        self.label_med = customtkinter.CTkLabel(master=self.frame_med, text="Medico: ", font=("Roboto Medium", -16))
        self.label_med.grid(row=2, column=2, columnspan=1, pady=5, padx=0, sticky="")

        self.label_dni = customtkinter.CTkLabel(master=self.frame_med, text="Dni: ", font=("Roboto Medium", -16))
        self.label_dni.grid(row=4, column=0, columnspan=1, pady=5, padx=0, sticky="")

        self.label_convenio = customtkinter.CTkLabel(master=self.frame_med, text="Convenio: ", font=("Roboto Medium", -16))
        self.label_convenio.grid(row=3, column=2, columnspan=1, pady=5, padx=0, sticky="")

        self.label_nroAsoc = customtkinter.CTkLabel(master=self.frame_med, text="Nro. Asociado: ", font=("Roboto Medium", -16))
        self.label_nroAsoc.grid(row=4, column=2, columnspan=1, pady=5, padx=0, sticky="")

        self.label_Warnings = customtkinter.CTkLabel(master=self.frame_med, text="", font=("Roboto Medium", -10))
        self.label_Warnings.grid(row=5, column=1, columnspan=1, pady=5, padx=0, sticky="")

        self.entry_Nombre = ttk.Entry(master=self.frame_med,text="",font=font.Font(family="Roboto Medium", size=10), state="disabled")
        self.entry_Apellido = ttk.Entry(master=self.frame_med,text="",font=font.Font(family="Roboto Medium", size=10), state="disabled")

        self.entry_Nombre.grid(row=1, column=1, columnspan=1, pady=5, padx=5, sticky="")
        self.entry_Apellido.grid(row=1, column=3, columnspan=1, pady=5, padx=5, sticky="")

        self.entry_Mail = ttk.Entry(master=self.frame_med,text="",font=font.Font(family="Roboto Medium", size=9), state="disabled")
        self.entry_Mail.grid(row=2, column=1, columnspan=1, pady=5, padx=5, sticky="")

        self.combobox_meds = customtkinter.CTkComboBox(master=self.frame_med,values=["Medico1","Medico2","Medico2"])
        self.combobox_meds.grid(row=2, column=3, columnspan=1, pady=10, padx=20, sticky="we")

        self.entry_Dni = ttk.Entry(master=self.frame_med,text="",font=font.Font(family="Roboto Medium", size=9), state="disabled")
        self.entry_Dni.grid(row=4, column=1, columnspan=1, pady=5, padx=5, sticky="")

        self.combobox_spec = customtkinter.CTkComboBox(master=self.frame_med,values=["Traumatologia", "Otorrinolaringologia", "Pediatria", "Cardiologia", "Clinico"])
        self.combobox_spec.grid(row=3, column=1, columnspan=1, pady=10, padx=20, sticky="we")

        self.optionMenu_conven = customtkinter.CTkOptionMenu(master=self.frame_med, values=["conv1", "conv2", "conv3"])
        self.optionMenu_conven.set("conv1")
        self.optionMenu_conven.grid(row=3, column=3, columnspan=1, pady=5, padx=5, sticky="")

        self.label_nroAsociado = customtkinter.CTkLabel(master=self.frame_med, text="", font=("Roboto Medium", -15))
        self.label_nroAsociado.grid(row=4, column=3, columnspan=1, pady=5, padx=5, sticky="")

        self.label_zona = customtkinter.CTkLabel(master=self.frame_med, text="Zona", font=("Roboto Medium", -15))
        self.label_zona.grid(row=5, column=0, columnspan=1, pady=5, padx=5, sticky="")

        self.optionMenu_Zona = customtkinter.CTkOptionMenu(master=self.frame_med, values=["CABA", "Cordoba", "Mendoza"])
        self.optionMenu_Zona.set("None")
        self.optionMenu_Zona.grid(row=5, column=1, columnspan=1, pady=5, padx=5, sticky="")

        self.button_crearTu = customtkinter.CTkButton(master=self.frame_med, text="Crear turno", border_width=2, fg_color=None, command=lambda: self.controlador.alta_turno(self))
        self.button_crearTu.grid(row=5, column=3, pady=5, padx=5)

        # Frame derecho
        self.button_crearAf = customtkinter.CTkButton(master=self.frame_der, text="Ingresar afiliado", border_width=2, fg_color=None, command=lambda: self.controlador.alta_afiliado())
        self.button_crearAf.grid(row=0, column=0, pady=5, padx=5)

        self.button_buscarAf = customtkinter.CTkButton(master=self.frame_der, text="Buscar afiliado", border_width=2, fg_color=None, command=lambda: self.controlador.buscar_afiliado(self.entry_Nombre,self.entry_Apellido, self.entry_Dni, self.entry_Mail, self.optionMenu_Zona, self.label_nroAsociado, self.button_modificarAf, self.label_Warnings, self.button_acepMod))
        self.button_buscarAf.grid(row=1, column=0, pady=5, padx=5)

        self.button_modificarAf = customtkinter.CTkButton(master=self.frame_der, text="Modificar afiliado", border_width=2, fg_color=None, state="disabled", command=lambda: self.controlador.modificar_afiliado(self.entry_Nombre,self.entry_Apellido,self.entry_Dni,self.entry_Mail))
        self.button_modificarAf.grid(row=2, column=0, pady=5, padx=5)
        self.button_acepMod = customtkinter.CTkButton(master=self.frame_med, text="Aceptar modificacion", border_width=2, fg_color=None, command=lambda: self.controladorAlta.ingresar_afiliado(self.label_Warnings,self.entry_Nombre,self.entry_Mail,self.entry_Dni,self.entry_Apellido,self.entry_Mail,self.optionMenu_Zona,None,"MODIFICAR",self.label_nroAsociado,self.button_acepMod))
        self.button_acepMod.configure(state="disabled")
        self.button_acepMod.grid(row=5, column=3, pady=5, padx=5)
      
 
if __name__ == "__main__":
    app = PanelPrincipal()
    app.mainloop()







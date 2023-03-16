####LIBRERiAS####

import tkinter
import customtkinter
import controlador_ingresar

from tkinter import *

#### ESTILO DE TKINTER ####
customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")


class PanelIngresarAfiliado(customtkinter.CTk):
   
   def __init__(self):
      super().__init__()

      self.controlador = controlador_ingresar.Controller()

      #Frame
      self.title("Crear usuario")
      self.geometry("610x220")  
      self.resizable(width=False, height=False)
      self.frame_form = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
      self.frame_form.grid(row=0, column=0, sticky="nswe")
    
    
      self.frame_form.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
      self.frame_form.rowconfigure((0, 1, 2, 3, 4, 5), minsize=10)
      self.frame_form.columnconfigure((0, 1, 2), weight=1)
      self.frame_form.columnconfigure((0, 1, 2), minsize=10)

      #Datos

      self.label_Warnings = customtkinter.CTkLabel(master=self.frame_form,text="", font=("Roboto Medium", -10))
      self.label_Warnings.grid(row=5, column=1, columnspan=1, pady=5, padx=0, sticky="")

      self.label_Nombre = customtkinter.CTkLabel(master=self.frame_form,text="Nombre", font=("Roboto Medium", -16))
      self.label_Nombre.grid(row=1, column=0, columnspan=1, pady=5, padx=0, sticky="")

      self.label_Apellido = customtkinter.CTkLabel(master=self.frame_form,text="Apellido:", font=("Roboto Medium", -16))
      self.label_Apellido.grid(row=1, column=2, columnspan=1, pady=5, padx=0, sticky="")

      self.entry_Nombre = customtkinter.CTkEntry(master=self.frame_form, placeholder_text="Nombre")
      self.entry_Apellido = customtkinter.CTkEntry(master=self.frame_form, placeholder_text="Apellido")

      self.entry_Nombre.grid(row=1, column=1, columnspan=1, pady=5, padx=5, sticky="")
      self.entry_Apellido.grid(row=1, column=3, columnspan=1, pady=5, padx=5, sticky="")

      self.label_Mail = customtkinter.CTkLabel(master=self.frame_form, text="Mail: ", font=("Roboto Medium", -16))
      self.label_Mail.grid(row=2, column=0, columnspan=1, pady=5, padx=0, sticky="")
      self.entry_Mail = customtkinter.CTkEntry(master=self.frame_form, placeholder_text="Correo electrnico")
      self.entry_Mail.grid(row=2, column=1, columnspan=1, pady=5, padx=5, sticky="")

      self.label_confMail = customtkinter.CTkLabel(master=self.frame_form, text="Confirmar correo: ", font=("Roboto Medium", -16))
      self.label_confMail.grid(row=2, column=2, columnspan=1, pady=5, padx=0, sticky="")
      self.entry_confMail = customtkinter.CTkEntry(master=self.frame_form, placeholder_text="Correo electronico")
      self.entry_confMail.grid(row=2, column=3, columnspan=1, pady=5, padx=5, sticky="")

      self.label_sexo = customtkinter.CTkLabel(master=self.frame_form, text="Sexo: ", font=("Roboto Medium", -16))
      self.label_sexo.grid(row=3, column=0, columnspan=1, pady=5, padx=0, sticky="")
      self.combobox_sexo = customtkinter.CTkComboBox(master=self.frame_form,values=["Masculino","Femenino"])
      self.combobox_sexo.grid(row=3, column=1, columnspan=1, pady=10, padx=20, sticky="we")

      self.label_dni = customtkinter.CTkLabel(master=self.frame_form, text="Dni: ", font=("Roboto Medium", -16))
      self.label_dni.grid(row=4, column=0, columnspan=1, pady=5, padx=0, sticky="")
      self.entry_Dni = customtkinter.CTkEntry(master=self.frame_form, placeholder_text="Dni")
      self.entry_Dni.grid(row=4, column=1, columnspan=1, pady=5, padx=5, sticky="")

      self.label_zona = customtkinter.CTkLabel(master=self.frame_form, text="Zona: ", font=("Roboto Medium", -16))
      self.label_zona.grid(row=3, column=2, columnspan=1, pady=5, padx=0, sticky="")
      self.optionMenu_zona = customtkinter.CTkOptionMenu(master=self.frame_form, values=["CABA", "Mendoza", "Cordoba"])
      self.optionMenu_zona.set("CABA")
      self.optionMenu_zona.grid(row=3, column=3, columnspan=1, pady=5, padx=5, sticky="")
      

      self.button_crearUs = customtkinter.CTkButton(master=self.frame_form, text="Agregar", border_width=2, fg_color=None, command=lambda : self.controlador.ingresar_afiliado(self.label_Warnings,self.entry_Nombre,self.entry_Mail,self.entry_Dni,self.entry_Apellido,self.entry_confMail,self.optionMenu_zona,self.combobox_sexo,"CREAR",None, None))
      self.button_crearUs.grid(row=4, column=3, pady=5, padx=5)
      self.attributes("-topmost", True)
      self.mainloop()


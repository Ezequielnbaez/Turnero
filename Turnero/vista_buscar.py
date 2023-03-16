####LIBRERIAS####

import tkinter
import customtkinter
import sqlite3
import re
import modelo
import controlador_buscar

from tkinter import *
from tkinter import font,ttk

#### ESTILO DE TKINTER ####
customtkinter.set_appearance_mode("light")  
customtkinter.set_default_color_theme("blue")


class PanelBuscar(customtkinter.CTk): 
    def __init__(self,entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf, label_WarningB,button_acepMod):
        super().__init__()

        self.controlador = controlador_buscar.Controller(entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf, label_WarningB,button_acepMod)

        # --------------------------------------------------
        # FRAME
        # --------------------------------------------------
        self.title("Buscar afiliado")
        self.geometry("620x220")
        self.resizable(width=False, height=True)
        self.frame_formB = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_formB.grid(row=0, column=0, sticky="nswe")

        self.frame_tree = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_tree.grid(row=1, column=0, sticky="nswe")

        self.frame_formB.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.frame_formB.rowconfigure((0, 1, 2, 3, 4, 5), minsize=10)
        self.frame_formB.columnconfigure((0, 1, 2, 3), weight=1)
        self.frame_formB.columnconfigure((0, 1, 2, 3), minsize=10)


        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------
        self.tree = ttk.Treeview(self.frame_tree, columns = (1,2,3,4,5,6), height = 10, show = "headings")
        self.tree.grid(row=1, column=0, columnspan=1, pady=0, padx=0, sticky="")

        self.tree.heading(1, text="Dni")
        self.tree.heading(2, text="NroAsociado")
        self.tree.heading(3, text="Nombre")
        self.tree.heading(4, text="Apellido")
        self.tree.heading(5, text="Mail")
        self.tree.heading(6, text="Zona")

        self.tree.column(1, width = 100)
        self.tree.column(2, width = 100)
        self.tree.column(3, width = 100)
        self.tree.column(4, width = 100)
        self.tree.column(5, width = 100)
        self.tree.column(6, width = 100)

        # Scrollbar
        self.scroll = ttk.Scrollbar(self.frame_tree, orient="vertical", command=self.tree.yview)
        self.scroll.grid(row=1, column=1, columnspan=1, pady=5, padx=0, sticky="")

        self.tree.configure(yscrollcommand=self.scroll.set)

        # Ingresos y Labels
        self.label_Bus = customtkinter.CTkLabel(master=self.frame_formB, text="Datos: ", font=("Roboto Medium", -16))
        self.label_Bus.grid(row=2, column=0, columnspan=1, pady=5, padx=0, sticky="")
        self.entry_Bus = customtkinter.CTkEntry(master=self.frame_formB, placeholder_text="Datos")
        self.entry_Bus.grid(row=2, column=1, columnspan=1, pady=5, padx=5, sticky="")

        self.label_WarningsB = customtkinter.CTkLabel(master=self.frame_formB, text="", font=("Roboto Medium", -10))
        self.label_WarningsB.grid(row=3, column=1, columnspan=1, pady=5, padx=0, sticky="")
        self.button_buscarUs = customtkinter.CTkButton(master=self.frame_formB, text="Buscar", border_width=2, fg_color=None, command=lambda : self.controlador.buscar(self.entry_Bus,self.label_WarningsB,self.tree))
        self.button_buscarUs.grid(row=2, column=3, pady=5, padx=5)
        self.button_seleccionarUs = customtkinter.CTkButton(master=self.frame_formB, text="Seleccionar", border_width=2, fg_color=None, command=lambda : self.controlador.seleccionar(self.tree,self.label_WarningsB))
        self.button_seleccionarUs.grid(row=2, column=4, pady=5, padx=5)
        self.button_eliminar = customtkinter.CTkButton(master=self.frame_formB, text="Eliminar", border_width=2, fg_color=None, command=lambda : self.controlador.eliminar(self.tree,self.label_WarningsB))
        self.button_eliminar.grid(row=3, column=4, pady=5, padx=5)

        self.attributes("-topmost", 1)
        self.mainloop()

if __name__ == "__vista_buscar__":
    app = PanelBuscar()
    app.mainloop()
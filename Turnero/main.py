####LIBRERiAS####

import tkinter
import customtkinter
import random #Se usara para generacion de nroAsociado
import sqlite3
import re
import modelo
import controlador 
import vista_principal
import vista_buscar
import vista_ingresar

from tkinter import *
from tkinter import font,ttk
from tkinter import messagebox



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        modeldb = modelo.Database()
        view = vista_principal.PanelPrincipal(self)
        controller = controlador.Controller(modeldb, view)

        view.micontrolador=controller
 

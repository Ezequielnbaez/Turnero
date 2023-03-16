from tkinter import Tk
import modelo

class Controller:
    def __init__(self,entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf, label_WarningB,button_acepMod):
         self.model = modelo.BSE(entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf,button_acepMod)

    def buscar(self,entry_Buscar,label_Warnings,tree):
         self.model.buscar_usuario(entry_Buscar,label_Warnings,tree)

    def eliminar(self,tree,label_Warnings):
         self.model.eliminar_usuario(tree,label_Warnings)
    
    def seleccionar(self,tree,label_Warnings):
         estado = self.model.seleccionar_usuario(tree,label_Warnings)
         label_Warnings.configure(text = estado)
         print(estado)
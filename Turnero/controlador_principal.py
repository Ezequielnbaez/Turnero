from tkinter import Tk
import vista_buscar
import vista_ingresar
import modelo

class Controller:
    def __init__(self,model): 
        self.model = model

    def alta_turno(instancia):
            modelo.check_turn(instancia)

    def alta_afiliado(self):
        vista_ingresar.PanelIngresarAfiliado()


    def buscar_afiliado(self,entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf, label_WarningB,button_acepMod):
        vista_buscar.PanelBuscar(entry_Nombre,entry_Apellido, entry_Dni, entry_Mail, optionMenu_Zona, label_nroAsociado, button_modificarAf, label_WarningB,button_acepMod)

    def modificar_afiliado(self,entry_Nombre,entry_Apellido, entry_Dni, entry_Mail):
        entry_Nombre.configure(state="normal")
        entry_Apellido.configure(state="normal")
        entry_Dni.configure(state="normal")
        entry_Mail.configure(state="normal")

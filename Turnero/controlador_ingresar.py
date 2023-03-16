from tkinter import Tk
import modelo
import observador

class Controller:
    def __init__(self):
         self.model = modelo.ABMU()
         self.obs = observador.ConcreteObserverA(self.model)

    def ingresar_afiliado(self,label_Warnings,entry_Nombre,entry_Mail
                                      ,entry_Dni,entry_Apellido,entry_confMail,
                                      optionMenu_zona,combobox_sexo,func,
                                      label_nroAsociado,button_acepMod):
    
        estado=self.model.check_datos(label_Warnings,entry_Nombre,entry_Mail
                                          ,entry_Dni,entry_Apellido,entry_confMail,
                                          optionMenu_zona,combobox_sexo,func,
                                          label_nroAsociado,button_acepMod)
        label_Warnings.configure(text = estado)
        
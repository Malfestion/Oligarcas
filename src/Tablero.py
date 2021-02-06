import random as rd
import numpy as np
from Jugador import jugador
from Negocio import Negocio
from Propiedad import Propiedad
import Opciones
Opciones.init()

BUEN_NEGOCIO=np.empty(Opciones.MAL_NEGOCIO, dtype=object)
MAL_NEGOCIO=np.empty(Opciones.BUEN_NEGOCIO, dtype=object)


class Tablero:
    global BUEN_NEGOCIO
    global MAL_NEGOCIO

    casillas=np.empty(Opciones.TAMANO, dtype=object)
    dados=[0,0,0]
    def avanzar(self,jugador,cantidad):
            jugador.avanzar(cantidad)
    def tirar_dados(self):
        self.dados[0]=rd.randint(1,6)
        self.dados[1]=rd.randint(1,6)
        self.dados[2]=self.dados[0]+self.dados[1]
        return self.dados[2]

    #TODO   
    def tiene_dominio(self,jugador,provincia):
        return 0
    #TODO  
    def init_negocios(self):
        return 0
    
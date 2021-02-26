import random as rd
import numpy as np
import csv
from Jugador import jugador
from Negocio import Negocio
from Propiedad import Propiedad
import Opciones
Opciones.init()
BUEN_NEGOCIO=np.empty(Opciones.MAL_NEGOCIO, dtype=object)
MAL_NEGOCIO=np.empty(Opciones.BUEN_NEGOCIO, dtype=object)


class Tablero:
    DATOS_GLOBALES=[]
    BUEN_NEGOCIO=[]
    MAL_NEGOCIO=[]
    PROPIEDADES=[]
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
    def init_data(self):
        with open('../media/data/gamedata.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.DATOS_GLOBALES.append(row)

    def init_negocios(self):
        print("No existen negocios disponibles, pendiente escribirlos")

    def init_propiedades(self):

        for prop in range(36):
            if prop!=0:
                propiedad=Propiedad(self.DATOS_GLOBALES[prop][0],self.DATOS_GLOBALES[prop][1],self.DATOS_GLOBALES[prop][2],self.DATOS_GLOBALES[prop][3],self.DATOS_GLOBALES[prop][4],self.DATOS_GLOBALES[prop][5],self.DATOS_GLOBALES[prop][6],self.DATOS_GLOBALES[prop][7])
                self.PROPIEDADES.append(propiedad)
        print("Se inician las propiedades correctamente.")

    def run_game(self):
        print("PENDIENTE: iniciar el juego")
    
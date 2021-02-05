import Opciones

class jugador:
    posicion=0
    dinero=0
    propiedades_total=0
    provincias={0,0,0,0,0,0,0}
    empresas=0
    medios=0

    def avanzar(self,cantidad):
        self.posicion=(self.posicion+cantidad)%Opciones.TAMANO
    

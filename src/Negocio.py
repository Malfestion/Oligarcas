class Negocio:
    bueno=True
    info=""
    dinero=0
    
    def imprimirDatos(self):

        if self.bueno==True:
            print("Buen Negocio!")
        else:
            print("Mal Negocio!")

        print(self.info)

        if self.bueno==True:
            print("El banco le da:",self.dinero,"colones.")
        else:
            print("Se rebaja de su dinero:",self.dinero,"colones.")


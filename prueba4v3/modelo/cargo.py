class Cargo:
    def __init__(self,numero=0,nombre=""):
        self.__identicaCargo = numero
        self.__descripcionCargo = nombre
        self.__listaCargo = {}

    def __str__(self):
        return f"{self.__identicaCargo} {self.__descripcionCargo}"

    #Getters
    def getIdenticaCargo(self):
        return self.__identicaCargo
    def getDescripcionCargo(self):
        return self.__descripcionCargo

    #Setters
    def setIdenticaCargo(self,numero):
        self.__identicaCargo=numero
    def setDescripcionCargo(self,nombre):
        self.__descripcionCargo=nombre

    #Métodos
    def addCargo(self, numero, nombre):
        existe = self.findCargo(numero)
        if existe is None:
            e = Cargo(numero, nombre)
            self.__listaCargo[numero] = e
            return(f'{nombre} ingresado correctamente')
        else:
            return(f'Cargo ya existe')

    def updateCargo(self, numero, nombre):
        e = self.findCargo(numero)
        if e is not None:
            e.setDescripcionCargo(nombre)
            return (f'Nuevo nombre: {e.getDescripcionCargo()}')
        else:
            return ('Cargo no encontrado')

    def delCargo(self, numero):
        e = self.findCargo(numero)
        if e is not None:
            self.__listaCargo.pop(numero)
            return(f'{e.getDescripcionCargo()} eliminado exitosamente!')
        else:
            return('Cargo no encontrado');

    def findCargo(self, numero):
        if len(self.__listaCargo) != 0:
            for a in self.__listaCargo.values():
                if numero == a.getIdenticaCargo():
                    return a;

    def findNombreCargo(self, numero):
        if len(self.__listaCargo) != 0:
            for a in self.__listaCargo.values():
                if numero == a.getIdenticaCargo():
                    return a.getDescripcionCargo();

    def findCargoByNombre(self, nombre):
        if len(self.__listaCargo) != 0:
            for a in self.__listaCargo.values():
                if nombre == a.getDescripcionCargo():
                    return a;

    def findAllCargos(self):
        if len(self.__listaCargo) != 0:
            for a in self.__listaCargo.values():
                print(a)
        else:
            print('No hay cargos para mostrar')
    
    def actualizarListaCargo(self, numero, nombre):
        existe = self.findCargo(numero)
        if existe is None:
            e = Cargo(numero, nombre)
            self.__listaCargo[numero] = e

listaCargo = Cargo()
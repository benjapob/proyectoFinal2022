class Comuna:
    def __init__(self,numero=0,nombre=""):
        self.__identicaComuna= numero
        self.__descripcionComuna = nombre
        self.__listaComuna = {}

    def __str__(self):
        return f"{self.__identicaComuna} {self.__descripcionComuna}"
    
    #Getters
    def getIdenticaComuna(self):
        return self.__identicaComuna
    def getDescripcionComuna(self):
        return self.__descripcionComuna
        
    #Setters
    def setIdenticaComuna(self,numero):
        self.__identicaComuna=numero
    def setDescripcionComuna(self,nombre):
        self.__descripcionComuna=nombre
    
    #Métodos
    def addComuna(self, numero, nombre):
        existe = self.findComuna(numero)
        if existe is None:
            e = Comuna(numero, nombre)
            self.__listaComuna[numero] = e
            return(f'{e.getDescripcionComuna()} ingresada correctamente')
        else:
            return('Comuna ya existe')

    def updateComuna(self, numero, nombre):
        e = self.findComuna(numero)
        if e is not None:
            e.setDescripcionComuna(nombre)
            return(f'Nuevo nombre: {e.getDescripcionComuna()}')
        else:
            return('Comuna no encontrada')

    def delComuna(self, numero):
        e = self.findComuna(numero)
        if e is not None:
            self.__listaComuna.pop(numero)
            return(f'{e.getDescripcionComuna()} eliminada exitosamente!')
        else:
            return('Comuna no encontrada');

    def findComuna(self, numero):
        if len(self.__listaComuna) != 0:
            for a in self.__listaComuna.values():
                if numero == a.getIdenticaComuna():
                    return a;

    def findNombreComuna(self, numero):
        if len(self.__listaComuna) != 0:
            for a in self.__listaComuna.values():
                if numero == a.getIdenticaComuna():
                    return a.getIdenticaComuna();


    def findComunaByNombre(self, nombre):
        if len(self.__listaComuna) != 0:
            for a in self.__listaComuna.values():
                if nombre == a.getDescripcionComuna():
                    return a;

    def findAllComunas(self):
        if len(self.__listaComuna) != 0:
            for a in self.__listaComuna.values():
                print(a)
        else:
            print('No hay comunas para mostrar')
    
    def actualizarListaComuna(self, numero, nombre):
        existe = self.findComuna(numero)
        if existe is None:
            e = Comuna(numero, nombre)
            self.__listaComuna[numero] = e

listaComuna = Comuna()
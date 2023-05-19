from modelo.cargo import Cargo, listaCargo
from modelo.comuna import Comuna, listaComuna
from utils.encoder import Encoder

class Empleado:
    def __init__(self,run="",nombre="", apellido="", cargo=Cargo(),direccion="",clave="",correo="",comuna=Comuna()):
            self.__runEmpleado = run
            self.__nombreEmpleado = nombre
            self.__apellidoEmpleado = apellido
            self.__cargo = cargo
            self.__direccionEmpleado = direccion
            self.__claveEmpleado = clave
            self.__correoEmpleado = correo
            self.__comuna = comuna
            self.__listaEmpleado = {}

    def __str__(self):
        #Str debería entregar solo el nombre de la comuna/cargo
        return f"{self.__runEmpleado}, {self.__nombreEmpleado}, {self.__apellidoEmpleado}, {self.getNombreCargo()}, {self.__direccionEmpleado}, {self.__correoEmpleado}, {self.getNombreComuna()}"
    
    #Getters
    def getRunEmpleado(self):
        return self.__runEmpleado
    def getNombreEmpleado(self):
        return self.__nombreEmpleado
    def getApellidoEmpleado(self):
        return self.__apellidoEmpleado
    def getCargo(self):
        return self.__cargo
    def getDireccionEmpleado(self):
        return self.__direccionEmpleado
    def getClaveEmpleado(self):
        return self.__claveEmpleado
    def getCorreoEmpleado(self):
        return self.__correoEmpleado
    def getComuna(self):
        return self.__comuna

    #Getters adicionales
    def getNombreCargo(self):
        return self.__cargo.getDescripcionCargo()
    def getNombreComuna(self):
        return self.__comuna.getDescripcionComuna()

    #Setters
    def setRunEmpleado(self,run):
        self.__runEmpleado=run
    def setNombreEmpleado(self,nombre):
        self.__nombreEmpleado=nombre
    def setApellidoEmpleado(self,apellido):
        self.__apellidoEmpleado=apellido
    def setCargo(self,cargo):
        self.__cargo=cargo
    def setDireccionEmpleado(self,direccion):
        self.__direccionEmpleado=direccion
    def setClaveEmpleado(self,clave):
        self.__claveEmpleado=Encoder().encode(clave)
    def setCorreoEmpleado(self, correo):
        self.__correoEmpleado=correo
    def setComuna(self,comuna):
        self.__comuna=comuna

    #Metodos
    def addEmpleado(self, cargo, comuna, run, nombre, apellido, direccion, clave, correo):
        #Comprobación de cargo y comuna en el dto, borrar comprobación
        e = Empleado(run, nombre, apellido, cargo, direccion, clave, correo, comuna)
        self.__listaEmpleado[run] = e
        return (f'Empleado rut: {run} agregado exitosamente!')
            
    def delEmpleado(self, run):
        e = self.findEmpleado(run)
        if e is not None:
            self.__listaEmpleado.pop(run)
            return (f'Empleado rut: {run} eliminado exitosamente!')

    def updateEmpleado(self, run, nombre, apellido, cargo, direccion, comuna):
        e = self.findEmpleado(run)
        if e is not None:
            e.setNombreEmpleado(nombre) if nombre != '' else None
            e.setApellidoEmpleado(apellido) if apellido != '' else None
            e.setCargo(cargo) if cargo.getDescripcionCargo() != '' else None
            e.setDireccionEmpleado(direccion) if direccion != '' else None
            e.setComuna(comuna) if comuna.getDescripcionComuna() != '' else None
            return (f'Nuevos datos: {e}')
        
    def findEmpleado(self, run):
        if len(self.__listaEmpleado) != 0:
            for a in self.__listaEmpleado.values():
                if a.getRunEmpleado() == run:
                    return a

    def findEmpleadoByComuna(self, comuna):
        if len(self.__listaEmpleado) != 0:
            listaCo = []
            for a in self.__listaEmpleado.values():
                if a.getComuna() == comuna:
                    listaCo.append(a)
            return listaCo

    def findEmpleadoByCargo(self, cargo):
        if len(self.__listaEmpleado) != 0:
            listaCa = []
            for a in self.__listaEmpleado.values():
                if a.getCargo() == cargo:
                    listaCa.append(a)
            return listaCa

    def findAllEmpleados(self):
        if len(self.__listaEmpleado) != 0:
            for a in self.__listaEmpleado.values():
                print(a)
        else:
            print('No hay empleados para mostrar')

    def actualizarListaEmpleado(self, run, nombre, apellido, cargo, direccion, clave, correo, comuna):
        e = Empleado(run, nombre, apellido, listaCargo.findCargo(cargo), direccion, clave, correo, listaComuna.findComuna(comuna))
        self.__listaEmpleado[run] = e

    def findAllEmpleados(self):
        if len(self.__listaEmpleado) != 0:
            for a in self.__listaEmpleado.values():
                print(a)
        else:
            print('No hay empleados para mostrar')

listaEmpleado = Empleado()
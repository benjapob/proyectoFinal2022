from modelo.empleado import Empleado, listaEmpleado
from modelo.comuna import Comuna, listaComuna
from modelo.cargo import Cargo, listaCargo 
from dao.dao_emp import daoEmp
from utils.encoder import Encoder

class EmpDTO:

    def validarLogin(self, correo, clave):
        daoemp = daoEmp()
        resultado = daoemp.validarLogin(Empleado(correo=correo, clave=Encoder().encode(clave)))
        return Empleado(nombre=resultado[0], apellido=resultado[1]) if resultado is not None else None

    def listarEmpleados(self):
        daoemp = daoEmp()
        daoemp.listarEmpleados();

    def actualizarListaEmpleado(self):
        daoemp = daoEmp()
        daoemp.actualizarListaEmpleado()

    def buscarEmpleadoComuna(self, comuna):
        existeComuna = listaComuna.findComunaByNombre(comuna.upper())
        if existeComuna is not None:
            daoemp = daoEmp()
            lista = daoemp.buscarEmpleadoComuna(Empleado(comuna=existeComuna))
            return lista if lista is not None else None

    def buscarEmpleadoCargo(self, cargo):
        existeCargo = listaCargo.findCargoByNombre(cargo.upper())
        if existeCargo is not None:
            daoemp = daoEmp()
            lista = daoemp.buscarEmpleadoCargo(Empleado(cargo=existeCargo))
            return lista if lista is not None else None

    def buscarEmpleado(self, run):
        daoemp = daoEmp()
        resultado = daoemp.buscarEmpleado(Empleado(run))
        return resultado if resultado is not None else None

    #Validar que no exista empleado, que exista el cargo y que exista la comuna para add, del y update
    def agregarEmpleado(self, run, nombre, apellido, cargo, direccion, clave, correo, comuna):
        existeEmp = self.buscarEmpleado(run)
        existeCargo = listaCargo.findCargoByNombre(cargo.upper())
        existeComuna = listaComuna.findComunaByNombre(comuna.upper())
        if existeEmp is None and existeCargo is not None and existeComuna is not None:
            daoemp = daoEmp()
            resultado = daoemp.agregarEmpleado(Empleado(run, nombre, apellido, existeCargo, direccion, Encoder().encode(clave), correo, existeComuna))
            return resultado
        else:
            resultado = 'Empleado ya existe y/o cargo o comuna no existe'
            return resultado

    def actualizarEmpleado(self, run, nombre, apellido, cargo, direccion, comuna):
        existeEmp = self.buscarEmpleado(run)
        existeCargo = listaCargo.findCargoByNombre(cargo.upper())
        existeComuna = listaComuna.findComunaByNombre(comuna.upper())
        if existeEmp is not None and existeCargo is not None and existeComuna is not None:
            daoemp = daoEmp()
            resultado = daoemp.actualizarEmpleado(Empleado(run, nombre, apellido, existeCargo, direccion, comuna=existeComuna))
            return resultado
        elif existeEmp is not None and cargo == '' and comuna == '':
            daoemp = daoEmp()
            resultado = daoemp.actualizarEmpleado(Empleado(run, nombre, apellido, cargo=Cargo(), direccion=direccion, comuna=Comuna()))
            return resultado
        else:
            resultado = 'Empleado, cargo o comuna no existe'
            return resultado
    
    def eliminarEmpleado(self, run):
        existe = self.buscarEmpleado(run)
        if existe is not None:
            conf = input(f"¿Estás seguro que quieres eliminar el Empleado rut: {existe.getRunEmpleado()}? (Escribe s para confirmar): ")
            if conf == 's':
                daoemp = daoEmp()
                resultado = daoemp.eliminarEmpleado(Empleado(run))
                return resultado
            else:
                resultado = 'No se realizaron cambios'
                return resultado
        else:
            resultado = 'Empleado no existe'
            return resultado

    
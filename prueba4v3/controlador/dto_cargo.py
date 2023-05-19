from modelo.cargo import Cargo
from dao.dao_cargo import daoCargo

class CargoDTO:

    def actualizarListaCargo(self):
        daocargo = daoCargo()
        daocargo.actualizarListaCargo()

    def listarCargos(self):
        daocargo = daoCargo()
        daocargo.listarCargos();

    def buscarCargo(self, numero):
        daocargo = daoCargo()
        resultado = daocargo.buscarCargo(Cargo(numero))
        return resultado if resultado is not None else None

    def activoCargo(self, numero):
        daocargo = daoCargo()
        resultado = daocargo.activoCargo(Cargo(numero))
        return resultado if resultado is not None else None

    def actualizarCargo(self, numero, nombre):
        existe = self.buscarCargo(numero)
        if existe is not None:
            daocargo = daoCargo()
            resultado = daocargo.actualizarCargo(Cargo(numero, nombre.upper()))
            return resultado
        else:
            resultado = 'Cargo no existe'
            return resultado

    def agregarCargo(self, numero, nombre):
        existe = self.buscarCargo(numero)
        if existe is None:
            daocargo = daoCargo()
            resultado = daocargo.agregarCargo(Cargo(numero, nombre.upper()))
            return resultado
        else:
            resultado = 'Cargo ya existe'
            return resultado

    def eliminarCargo(self, numero):
        existe = self.buscarCargo(numero)
        activo = self.activoCargo(numero)
        if existe is not None and len(activo) == 0:
            conf = input(f"¿Estás seguro que quieres eliminar el cargo {existe.getDescripcionCargo()}? (Escribe s para confirmar): ")
            if conf == 's':
                daocargo = daoCargo()
                resultado = daocargo.eliminarCargo(Cargo(numero))
                return resultado
            else:
                resultado = 'No se realizaron cambios'
                return resultado
        else:
            resultado = 'Cargo no existe o está en uso'
            return resultado
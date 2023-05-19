from modelo.comuna import Comuna
from dao.dao_comuna import daoComuna

class ComunaDTO:

    def actualizarListaComuna(self):
        daocomuna = daoComuna()
        daocomuna.actualizarListaComuna()

    def listarComunas(self):
        daocomuna = daoComuna()
        daocomuna.listarComunas();

    def buscarComuna(self, numero):
        daocomuna = daoComuna()
        resultado = daocomuna.buscarComuna(Comuna(numero))
        return resultado if resultado is not None else None

    def activoComuna(self, numero):
        daocomuna = daoComuna()
        resultado = daocomuna.activoComuna(Comuna(numero))
        return resultado if resultado is not None else None

    def actualizarComuna(self, numero, nombre):
        existe = self.buscarComuna(numero)
        if existe is not None:
            daocomuna = daoComuna()
            resultado = daocomuna.actualizarComuna(Comuna(numero, nombre.upper()))
            return resultado
        else:
            resultado = 'Comuna no existe'
            return resultado

    def agregarComuna(self, numero, nombre):
        existe = self.buscarComuna(numero)
        if existe is None:
            daocomuna = daoComuna()
            resultado = daocomuna.agregarComuna(Comuna(numero, nombre.upper()))
            return resultado
        else:
            resultado = 'Comuna ya existe'
            return resultado

    def eliminarComuna(self, numero):
        existe = self.buscarComuna(numero)
        activo = self.activoComuna(numero)
        if existe is not None and len(activo) == 0:
            conf = input(f"¿Estás seguro que quieres eliminar la comuna {existe.getDescripcionComuna()}? (Escribe s para confirmar): ")
            if conf == 's':
                daocomuna = daoComuna()
                resultado = daocomuna.eliminarComuna(Comuna(numero))
                return resultado
            else:
                resultado = 'No se realizaron cambios'
                return resultado
        else:
            resultado = 'Comuna no existe o está en uso'
            return resultado
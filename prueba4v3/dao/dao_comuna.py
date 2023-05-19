from conex import conn
from modelo.comuna import listaComuna
import traceback

class daoComuna:
    def __init__(self):
        try:
            #Profe le hice la vida más fácil, ahora no tiene que cambiar el nombre de la BD a poo3
            self.conn = conn.Conex("localhost", "root", "", "poo3")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def actualizarListaComuna(self):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select numerocomuna, nombrecomuna from comuna")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    listaComuna.actualizarListaComuna(a[0], a[1])
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
                
    def listarComunas(self):
        listaComuna.findAllComunas();

    def buscarComuna(self, comuna):
        resultado = listaComuna.findComuna(comuna.getIdenticaComuna())
        return resultado;

    def activoComuna(self, comuna):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(f"""
                                select com.numerocomuna
                                from empleado emp, cargo car, comuna com
                                where emp.idcargo = car.idcargo and 
                                    emp.idcomuna = com.idcomuna
                                and com.numerocomuna = {comuna.getIdenticaComuna()}
                                order by emp.idempleado; 

                                """)
            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado

    def actualizarComuna(self, comuna):
        param = "set @param = %s;" 
        sql = "update comuna set nombrecomuna = case when @param='' then nombrecomuna else @param end where numerocomuna = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(param, (comuna.getDescripcionComuna(),))
            cursor.execute(sql, (comuna.getIdenticaComuna(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaComuna.updateComuna(comuna.getIdenticaComuna(), comuna.getDescripcionComuna())
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def agregarComuna(self,comuna):
        sql = "insert into comuna values (null,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.getIdenticaComuna(),comuna.getDescripcionComuna()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaComuna.addComuna(comuna.getIdenticaComuna(),comuna.getDescripcionComuna());
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def eliminarComuna(self, comuna):
        sql = "delete from comuna where numerocomuna = %s"
        mensaje = ""
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (comuna.getIdenticaComuna(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaComuna.delComuna(comuna.getIdenticaComuna())
            else:
                mensaje="No se realizaron cambios"
        
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex() 
        return mensaje




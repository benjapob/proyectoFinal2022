from conex import conn
from modelo.cargo import listaCargo
import traceback

class daoCargo:
    def __init__(self):
        try:
            #Profe le hice la vida más fácil, ahora no tiene que cambiar el nombre de la BD a poo3
            self.conn = conn.Conex("localhost", "root", "", "poo3")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def actualizarListaCargo(self):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select numerocargo, nombrecargo from cargo")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    listaCargo.actualizarListaCargo(a[0], a[1])
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
                
    def listarCargos(self):
        listaCargo.findAllCargos();

    def buscarCargo(self, cargo):
        resultado = listaCargo.findCargo(cargo.getIdenticaCargo())
        return resultado;

    def activoCargo(self, cargo):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(f"""
                                select car.numerocargo
                                from empleado emp, cargo car, comuna com
                                where emp.idcargo = car.idcargo and 
                                    emp.idcomuna = com.idcomuna
                                and car.numerocargo = {cargo.getIdenticaCargo()}
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

    def actualizarCargo(self, cargo):
        param = "set @param = %s;" 
        sql = "update cargo set nombrecargo = case when @param='' then nombrecargo else @param end where numerocargo = %s"
        mensaje = ""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(param, (cargo.getDescripcionCargo(),))
            cursor.execute(sql, (cargo.getIdenticaCargo(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaCargo.updateCargo(cargo.getIdenticaCargo(), cargo.getDescripcionCargo())
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def agregarCargo(self,cargo):
        sql = "insert into cargo values (null,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdenticaCargo(),cargo.getDescripcionCargo()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaCargo.addCargo(cargo.getIdenticaCargo(),cargo.getDescripcionCargo());
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def eliminarCargo(self, cargo):
        sql = "delete from cargo where numerocargo = %s"
        mensaje = ""
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (cargo.getIdenticaCargo(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaCargo.delCargo(cargo.getIdenticaCargo())
            else:
                mensaje="No se realizaron cambios"
        
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex() 
        return mensaje




from conex import conn
from modelo.empleado import listaEmpleado
import traceback

class daoEmp:
    def __init__(self):
        try:
            #Profe le hice la vida más fácil, ahora no tiene que cambiar el nombre de la BD a poo3
            self.conn = conn.Conex("localhost", "root", "", "poo3")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def validarLogin(self, emp):
        sql = "select nombre, apellido from empleado where correo = %s and clave = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql,(emp.getCorreoEmpleado(), emp.getClaveEmpleado()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return resultado

    def actualizarListaEmpleado(self):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select run, nombre, apellido, idcargo, direccion, clave, correo, idcomuna from empleado")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    cursor.execute(f"select numerocargo from cargo where idcargo = {a[3]}")
                    numCargo = cursor.fetchone()
                    
                    cursor.execute(f"select numerocomuna from comuna where idcomuna = {a[7]}")
                    numComuna = cursor.fetchone()
                    
                    listaEmpleado.actualizarListaEmpleado(a[0], a[1], a[2], numCargo[0], a[4], a[5], a[6], numComuna[0])
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()

    def listarEmpleados(self):
        listaEmpleado.findAllEmpleados();

    def buscarEmpleado(self, empleado):
        resultado = listaEmpleado.findEmpleado(empleado.getRunEmpleado())
        return resultado;

    def actualizarEmpleado(self, empleado):
        param = "set @nombre = %s;"
        param2 = "set @apellido = %s;"
        param3 = "set @idcargo = %s;"
        param4 = "set @direccion = %s;"
        param5 = "set @idcomuna = %s;"
        sql = """update empleado set nombre = case when @nombre='' then nombre else @nombre end, 
        apellido = case when @apellido='' then apellido else @apellido end, 
        idcargo = case when @idcargo='' then idcargo else @idcargo end, 
        direccion = case when @direccion='' then direccion else @direccion end, 
        idcomuna = case when @idcomuna='' then idcomuna else @idcomuna end where run = %s"""
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(f"select idcargo from cargo where numerocargo = {empleado.getCargo().getIdenticaCargo()}")
            idCargo = cursor.fetchone()
            if idCargo is None:
                idCargo = ['']
            cursor.execute(f"select idcomuna from comuna where numerocomuna = {empleado.getComuna().getIdenticaComuna()}")
            idComuna = cursor.fetchone()
            if idComuna is None:
                idComuna = ['']
            cursor.execute(param, (empleado.getNombreEmpleado(),))
            cursor.execute(param2, (empleado.getApellidoEmpleado(),))
            cursor.execute(param3, (idCargo[0],))
            cursor.execute(param4, (empleado.getDireccionEmpleado(),))
            cursor.execute(param5, (idComuna[0],))
            cursor.execute(sql, (empleado.getRunEmpleado(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaEmpleado.updateEmpleado(empleado.getRunEmpleado(), empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getCargo(), empleado.getDireccionEmpleado(), empleado.getComuna())
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def agregarEmpleado(self,empleado):
        sql = "insert into empleado values (null,%s,%s,%s,%s,%s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(f"select idcargo from cargo where numerocargo = {empleado.getCargo().getIdenticaCargo()}")
            idCargo = cursor.fetchone()
            cursor.execute(f"select idcomuna from comuna where numerocomuna = {empleado.getComuna().getIdenticaComuna()}")
            idComuna = cursor.fetchone()
            cursor.execute(sql, (idCargo[0], idComuna[0], empleado.getRunEmpleado(), empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getDireccionEmpleado(), empleado.getClaveEmpleado(), empleado.getCorreoEmpleado()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaEmpleado.addEmpleado(empleado.getCargo(), empleado.getComuna(), empleado.getRunEmpleado(), empleado.getNombreEmpleado(), empleado.getApellidoEmpleado(), empleado.getDireccionEmpleado(), empleado.getClaveEmpleado(), empleado.getCorreoEmpleado());
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def eliminarEmpleado(self, empleado):
        sql = "delete from empleado where run = %s"
        mensaje = ""
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (empleado.getRunEmpleado(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = listaEmpleado.delEmpleado(empleado.getRunEmpleado())
            else:
                mensaje="No se realizaron cambios"
        
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex() 
        return mensaje

    def buscarEmpleadoComuna(self, empleado):
        resultado = listaEmpleado.findEmpleadoByComuna(empleado.getComuna())
        return resultado;

    def buscarEmpleadoCargo(self, empleado):
        resultado = listaEmpleado.findEmpleadoByCargo(empleado.getCargo())
        return resultado;
    

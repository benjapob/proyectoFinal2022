from controlador.dto_emp import EmpDTO
from controlador.dto_cargo import CargoDTO
from controlador.dto_comuna import ComunaDTO

#Validaciones y utilidades

def volver():
    input("Presione enter para volver...\n")

def continuar():
    input("Presione enter para continuar...\n");

def actualizarListaCargo():
    CargoDTO().actualizarListaCargo();

def actualizarListaComuna():
    ComunaDTO().actualizarListaComuna();

def actualizarListaEmpleado():
    EmpDTO().actualizarListaEmpleado();

def validarCorreo():
    try:
        correo = input(f'Ingresar correo: ' )
        if '@' in correo:
            return correo
        else:
            print("Debe ingresar un correo válido")
            return validarCorreo();
    except:
        print("Debe ingresar un correo válido")
        return validarCorreo();

def validarRut():
    try:
        rut = input(f'Ingresar rut (sin puntos y con guión): ' )
        if len(rut) >= 9 and len(rut) <= 10:
            return rut
        else:
            print("Debe ingresar un rut válido")
            return validarRut();
    except:
        print("Debe ingresar un rut válido")
        return validarRut();

def validarInt(cadena):
        try:
            numero = int(input(f'Ingresar {cadena} (sólo números): ' ))
            if numero > 0:
                return numero
            else:
                print("Debe ingresar un número válido")
                return validarInt(cadena);
        except:
            print("Debe ingresar un número válido")
            return validarInt(cadena);

def validarFloat(cadena):
        try:
            numero = float(input(f'Ingresar {cadena} (sólo números): ' ))
            if numero > 0:
                return numero
            else:
                print("Debe ingresar un número válido")
                return validarFloat(cadena);
        except:
            print("Debe ingresar un número válido")
            return validarFloat(cadena);

def validarStr(cadena):
        try:
            string = input(f'Ingresar {cadena}: ' )
            if len(string) > 0:
                return string
            else:
                print("El campo no puede estar vacío")
                return validarStr(cadena);
        except:
            print("El campo no puede estar vacío")
            return validarStr(cadena);

def validarLogin():
    resultado = EmpDTO().validarLogin(validarStr('correo'), validarStr('contraseña'));
    return resultado

#Funciones CRUD Comuna

def validaListarComunas():
    ComunaDTO().listarComunas();

def validaAgregarComuna():
    resultado = ComunaDTO().agregarComuna(validarInt('numero de la comuna'), validarStr('nombre de la comuna'));
    print(resultado);

def validaActualizarComuna():
    ComunaDTO().listarComunas();
    resultado = ComunaDTO().actualizarComuna(validarInt('numero de la comuna a editar'), input('Ingresar nuevo nombre de la comuna (Si no desea modificarlo, presione enter): '));
    print(resultado);

def validaEliminarComuna():
    ComunaDTO().listarComunas();
    resultado = ComunaDTO().eliminarComuna(validarInt('numero de la comuna a eliminar'))
    print(resultado)

#Funciones CRUD Cargo

def validaListarCargos():
    CargoDTO().listarCargos();

def validaAgregarCargo():
    resultado = CargoDTO().agregarCargo(validarInt('numero del cargo'), validarStr('nombre del cargo'));
    print(resultado);

def validaActualizarCargo():
    CargoDTO().listarCargos();
    resultado = CargoDTO().actualizarCargo(validarInt('numero del cargo a editar'), input('Ingresar nuevo nombre del cargo (Si no desea modificarlo, presione enter): '));
    print(resultado);

def validaEliminarCargo():
    CargoDTO().listarCargos();
    resultado = CargoDTO().eliminarCargo(validarInt('numero del cargo a eliminar'))
    print(resultado)

#Funciones CRUD Empleado

def validaEliminarEmpleado():
    EmpDTO().listarEmpleados();
    resultado = EmpDTO().eliminarEmpleado(validarStr('rut del empleado a eliminar'))
    print (resultado)

def validaActualizarEmpleado():
    EmpDTO().listarEmpleados();
    resultado = EmpDTO().actualizarEmpleado(validarStr('rut del empleado a modificar'), input('Ingresar nuevo nombre del empleado (Si no desea modificarlo, presione enter): '),input('Ingresar nuevo apellido del empleado (Si no desea modificarlo, presione enter): '), input('Ingresar nombre del cargo nuevo del empleado (Si no desea modificarlo, presione enter): '),input('Ingresar nueva dirección del empleado (Si no desea modificarlo, presione enter): '), input('Ingresar nombre de la comuna nueva del empleado (Si no desea modificarlo, presione enter): '))
    print(resultado)

def validaAgregarEmpleado():
    resultado = EmpDTO().agregarEmpleado(validarRut(), validarStr('nombre del empleado'),validarStr('apellido del empleado'), validarStr('nombre del cargo del empleado'),validarStr('dirección del empleado'), validarStr('clave del empleado'), validarCorreo(), validarStr('nombre de la comuna del empleado'));
    print(resultado);

def validaBuscarEmpleadoCargo():
    CargoDTO().listarCargos();
    lista = EmpDTO().buscarEmpleadoCargo(validarStr('nombre del cargo'))
    if lista is not None:
        if len(lista) != 0:
            for a in lista:
                print(a)
                print("")
        else:
            print('No hay empleados que tengan el cargo ingresado')
    else:
        print('El cargo ingresado no existe')

def validaBuscarEmpleadoComuna():
    ComunaDTO().listarComunas();
    lista = EmpDTO().buscarEmpleadoComuna(validarStr('nombre de la comuna'))
    if lista is not None:
        if len(lista) != 0:
            for a in lista:
                print(a)
                print("")
        else:
            print('No hay empleados que vivan en la comuna ingresada')
    else:
        print('La comuna ingresada no existe')

# Para llegar al menu primero hay que loguearse

def menu():
    print('-----CRUD MiniMarket Fénix-----')
    print("1. CRUD Empleados")
    print("2. CRUD Cargos")
    print("3. CRUD Comunas")
    print("4. Salir del sistema")
    opc = int( input("Ingrese una opción : "))
    print("")
    return opc

# Menú cargo

def menuCargo():
    print('-----CRUD Cargos-----')
    print("1. Ingresar Cargo")
    print("2. Modificar Cargo")
    print("3. Eliminar Cargo")
    print("4. Mostrar todos los Cargos")
    print("5. Volver al menú principal")
    opc = int( input("Ingrese una opción : "))
    print("")
    return opc

#Menú comuna

def menuComuna():
    print('-----CRUD Comunas-----')
    print("1. Ingresar Comuna")
    print("2. Modificar Comuna")
    print("3. Eliminar Comuna")
    print("4. Mostrar todos los Comunas")
    print("5. Volver al menú principal")
    opc = int( input("Ingrese una opción : "))
    print("")
    return opc

#Menú empleado

def menuEmpleado():
    print('-----CRUD Empleados-----')
    print("1. Ingresar Empleado")
    print("2. Modificar Empleado")
    print("3. Eliminar Empleado")
    print("4. Mostrar Empleados por cargo")
    print("5. Mostrar Empleados por comuna")
    print("6. Volver al menú principal")
    opc = int( input("Ingrese una opción : "))
    print("")
    return opc

#Menú inicial

def inicial():
    try:
        while True:
            opc = menu()
            if opc == 1:
                try:
                    while True:
                        opc = menuEmpleado()
                        if opc == 1:
                            validaAgregarEmpleado()
                            continuar();
                        elif opc == 2:
                            validaActualizarEmpleado()
                            continuar();
                        elif opc == 3:
                            validaEliminarEmpleado()
                            continuar();
                        elif opc == 4:
                            validaBuscarEmpleadoCargo()
                            continuar();
                        elif opc == 5:
                            validaBuscarEmpleadoComuna()
                            continuar();
                        elif opc == 6:
                            break;
                        else:
                            print('Opción no válida')
                            volver();
                except:
                    print('Opción no válida, volviendo al menú principal...')
                    volver()
            elif opc == 2:
                try:
                    while True:
                        opc = menuCargo()
                        if opc == 1:
                            validaAgregarCargo();
                            continuar();
                        elif opc == 2:
                            validaActualizarCargo();
                            continuar();
                        elif opc == 3:
                            validaEliminarCargo();
                            continuar();
                        elif opc == 4:
                            validaListarCargos();
                            continuar();
                        elif opc == 5:
                            break;
                        else:
                            print('Opción no válida')
                            volver();
                except:
                    print('Opción no válida, volviendo al menú principal...')
                    volver()
            elif opc == 3:
                try:
                    while True:
                        opc = menuComuna()
                        if opc == 1:
                            validaAgregarComuna();
                            continuar();
                        elif opc == 2:
                            validaActualizarComuna();
                            continuar();
                        elif opc == 3:
                            validaEliminarComuna();
                            continuar();
                        elif opc == 4:
                            validaListarComunas();
                            continuar();
                        elif opc == 5:
                            break;
                        else:
                            print('Opción no válida')
                            volver();
                except:
                    print('Opción no válida, volviendo al menú principal...')
                    volver()
            elif opc == 4:
                print("Saliendo...")
                break;
            else:
                print('Opción no válida')
                volver();
    except:
        print('Opción no válida')
        volver()
        inicial()

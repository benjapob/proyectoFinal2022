from controlador.validations import inicial, validarLogin, actualizarListaCargo, actualizarListaComuna, actualizarListaEmpleado

def volver():
    input("Presione enter para volver...\n")

def continuar():
    input("Presione enter para continuar...\n");
##### login
intentos = 1
print("Sistema CRUD")
while intentos <= 3:
    try:
        resu = validarLogin()
        if resu is not None:
            actualizarListaCargo()
            actualizarListaComuna()
            actualizarListaEmpleado()
            print(f"Bienvenido(a) Sr(a). : {resu.getNombreEmpleado()} {resu.getApellidoEmpleado()}")
            continuar()
            inicial()
            break
        else:
            print("correo o contraseña incorrecta")
            continuar()
            intentos += 1
    except:
        print("intentar nuevamente")
        volver()
if intentos == 4:
    print("contraseña bloqueada")
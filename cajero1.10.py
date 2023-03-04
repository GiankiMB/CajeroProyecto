import os
import datetime
import sys
from colorama import init,Fore,Style
from time import sleep
from tqdm.auto import tqdm
import stdiomask

#hola
administrador = 'admin'
admcontra = '1234'
contador = 0


def barra_carga():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ")
    espera = tqdm(total=2600, position=0, leave=False)
    for k in range (2600):
        espera.set_description(Fore.GREEN+"CARGANDO...".format(k).center(50))
        espera.update(1)
    espera.close()
os.system("cls")

def barra_carga2():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ")
        espera = tqdm(total=2700, position=0, leave=False)
        for k in range (2700):
            espera.set_description(Fore.GREEN+"GUARDADNDO CAMBIOS...".format(k).center(50))
            espera.update(1)
        espera.close()
        os.system("cls")

barra_carga()
# os.system("cls")
# sleep(1)

# init()
# print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\n\n\n\n\n\n\n                                                            /////                   ")
# sleep(0.05)                                             
# print("                                                            /////")
# sleep(0.05)
# print("                                                         *//////* ")
# sleep(0.05)
# print("                                                 *//////*      *//////*")
# sleep(0.05)
# print("                                                 *///////*          *//////*        ")          
# sleep(0.05)                                                       
# print("                                                 *//////*                          ")
# sleep(0.05)            
# print("                                                         *//////*                   ")        
# sleep(0.05)                                                   
# print("                                                             *//////*               ")       
# sleep(0.05)                                                    
# print("                                                 *//////*         *//////*          ")       
# sleep(0.05)                                                   
# print("                                                     *//////*           *//////*    ") 
# sleep(0.05)
# print("                                                    *//////*      *//////* ")
# print("                                                             *//////*")
# sleep(0.05)                                                            
# print("                                                             //////")
# sleep(0.05)                                                          
# print("                                                             //////")
# sleep(0.05)
# sleep(2)
# os.system("cls")


# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\n\n\n\n\n\n                                /////////////////                     /////////////                                              ")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////           ///                  ///         /// ")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////                               ///               ")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////                               ///                ")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////   ///////////     /////////   ///                   ////////////       ////////    /////////")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////            //        //       ///                   //        //      //     //    //     //")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////            //        //       ///                   //        //      ////////     /////////")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////            //        //       ///                   //        //      // //        //       ")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                ////            //        //       ///          ///      //        //      //  //       //       ")
# sleep(0.05)
# print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"                                //////////////////     ////////     //////////////       ////////////      //   ///     //       ")

# sleep(3)
# os.system("cls")

def contra():
    while True:
        try:
            print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\t\t\t\t\tLa contraseña debe tener 4 dijitos!")
            while True:
                contraclien = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\t⁃contraseña ➣ ")
                if len(contraclien) ==4:
                        return contraclien
                else:
                    os.system("cls")
                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tLa contraseña debe tener 4 dijitos!")
                    sleep(2)    
        except ValueError:
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tValor no valido")
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tIngrese un valor entero")
            os.system("pause")
            os.system("cls")
def validarced():
    while True:
        cdu = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tCedula ➣ ")
        suma = 0
        for i in range(len(cdu) - 1):
            x = int(cdu[i])
            if i%2 == 0:
                x = x * 2
                if x > 9:
                    x = x - 9
            suma = suma + x
        if suma%10 != 0:
            result = 10 - (suma%10)
            if int(cdu[-1]) == result:
                print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\t\t\t\t\tLa cedula {} es ecuatoriana".format(cdu))
                return cdu
            else:
                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tLa cedula {} no es ecuatoriana".format(cdu))

def valicorreo():
    while True:
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+'''\t\t\t\t\tIntroduzca un correo valido
            \t\t\t\t\tEjemplo@gmail.com    
        ''')
        correo = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tCorreo ➣ ")
        if "@" and  "." in correo:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\t\t\t\t\tEs válido")
            return correo
        else:
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tNo es válido")
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tEl correo debe contener @ y un punto(.) ")


def mayord():
    while True:
        edad = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tEscribe tu edad ➣ "))
        if edad >= 18:
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\t\t\t\t\tMayor de edad")
            return int(edad)
        else:
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tDebe ser mayor de edad para registrarse")


def pedirdatos():
    archivo = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tIngrese el nombre del archivo plano del nuevo Cliente: ")
    with open(archivo + ".txt", "a") as f:    
        nombre = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tNombre ➣ ")
        edad = mayord()
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\t\t\t\t\tIngrese una Cedula Ecuatotiana")
        cdu= validarced()
        ciudad = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tCiudad ➣ ")
        cell = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tTelefono ➣ ")
        correo = valicorreo()
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngresa un nombre de usuario cualquiera ")
        usu = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\t⁃Usuario ➣ ")
        contrausu = contra()
        saldo =input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\t⁃Ingresa el monto del Cliente ➣ ")
        f.write(cdu+","+usu+","+contrausu+","+saldo+","+nombre+","+ciudad+","+cell+","+correo+","+str(edad)+"\n")
        print(f"\t\t\t\t\tSe guardó la información en el archivo {archivo}.txt")
        sleep(2)
        os.system("cls")
        espera = tqdm(total=2600, position=0, leave=False)
        for k in range (2600):
            espera.set_description(Fore.BLUE+" GUARDANDO DATOS...".format(k))
            espera.update(1)
        espera.close()
        init()
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+ "\n\n\n\n\n\t\t\t\t\t\tSe ha guardado")  
        print("\t\t\t╔══════════════════════════════✧❂✧════════════════════════╗")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tNombre:"+ nombre + "\n\t\t\t\t\tedad:" + str(edad) +
        "\n\t\t\t\t\tCedula:" + cdu + "\n\t\t\t\t\tCiudad:"+ciudad +
        "\n\t\t\t\t\tTelefono:"+cell+"\n\t\t\t\t\tCorreo:"+ correo+"\n\t\t\t\t\tUsuario:"+ usu+
        "\n\t\t\t\t\tContraseña:"+ contrausu+"\n\t\t\t\t\tMonto:"+ saldo)
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t╚════════════════════════════════✧♛✧═══════════════════════╝")

        os.system("pause")
        os.system("cls")

def mostrardatos():
        archivoclientes= open("datos.txt","r")
        datosCuenta= archivoclientes.readline().strip().split(",")
        numeroCuenta= datosCuenta[0]
        nonmbreCuenta = datosCuenta[1]
        contraCuenta = datosCuenta[2]
        saldo =  int(datosCuenta[3])
        nonmbrecliente= datosCuenta[4]
        cuidacliente = datosCuenta[5]
        cellcliente = datosCuenta[6]
        correocliente =datosCuenta[7]
        edadcliente = datosCuenta[8]
        archivoclientes.close()
        
        barra_carga()
        os.system("cls")
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"Datos de Clientes".center(110))
        print("\t\t\t╔════════════════════════════✧❂✧══════════════════════════╗")
        print("\t\t\t                                                             ")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t            Cedula:             ",numeroCuenta)
        print("\t\t\t\t            Nombre de usuario:  ",nonmbreCuenta)
        print("\t\t\t\t            Contraseña:         ",contraCuenta)  
        print("\t\t\t\t            Saldo:              ",saldo)  
        print("\t\t\t\t            Nombre:             ",nonmbrecliente)
        print("\t\t\t\t            Ciudad:             ",cuidacliente) 
        print("\t\t\t\t            Celular:            ",cellcliente)
        print("\t\t\t\t            Correo:             ",correocliente)
        print("\t\t\t\t            Edad:               ",edadcliente) 
        print("\t\t\t\t                                                  ")
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t╚══════════════════════════════✧♛✧═════════════════════════╝")
        os.system("pause")
        os.system("cls")


def editar():
        archivoclientes= open("datos.txt","r")
        datosCuenta= archivoclientes.readline().strip().split(",")
        numeroCuenta= datosCuenta[0]
        nonmbreCuenta = datosCuenta[1]
        contraCuenta = datosCuenta[2]
        saldo =  int(datosCuenta[3])
        nonmbrecliente= datosCuenta[4]
        cuidacliente = datosCuenta[5]
        cellcliente = datosCuenta[6]
        correocliente =datosCuenta[7]
        edadcliente = datosCuenta[8]
        archivoclientes.close()

        while True:
            barra_carga2()
            os.system("cls")
            print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"Datos de Clientes".center(120))
            print("\t\t\t╔════════════════════════════✧❂✧══════════════════════════╗")
            print("\t\t\t                                                             ")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t         1) Cedula:           ",numeroCuenta)
            print("\t\t\t\t         2) Nombre de usuario:",nonmbreCuenta)
            print("\t\t\t\t         3) Contraseña:       ",contraCuenta)  
            print("\t\t\t\t         4) Saldo:            ",saldo)  
            print("\t\t\t\t         5) Nombre:           ",nonmbrecliente)  
            print("\t\t\t\t         6) Ciudad:           ",cuidacliente) 
            print("\t\t\t\t         7) Celular:          ",cellcliente)
            print("\t\t\t\t         8) Correo:           ",correocliente)
            print("\t\t\t\t         9) Edad:             ",edadcliente)
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t                                          0) Salir  ")
            print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t╚══════════════════════════════✧♛✧═════════════════════════╝")

            op = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\tIngrese la opcion que desea cambiar ➣ "))
            if op ==1:
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese la nueva Cedula ")
                cdu = validarced()
                numeroCuenta = cdu
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()


            elif op ==2:
                nuevousu = input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese el nuevo nombre de usuario ➣ ")
                nonmbreCuenta = nuevousu
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==3:
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese la nueva contraseña ")
                nuevacontra = contra()
                contraCuenta = nuevacontra
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==4:
                nuevousaldo = input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese el nuevo saldo ➣ ")
                saldo = nuevousaldo
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==5:
                nuevonom = input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese el nuevo Nombre ➣ ")
                nonmbrecliente = nuevonom
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==6:
                nuevaciu = input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese la nueva información ➣ ")
                cuidacliente = nuevaciu
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==7:
                nuevocell = input(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese el nuevo número celular ➣ ")
                cellcliente = nuevocell
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==8:
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese el nuevo correo  ")
                nuevocorreo = valicorreo()
                correocliente = nuevocorreo
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op == 9:
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t\tIngrese la nueva información  ")
                edadcliente = mayord()
                os.system("cls")
                archivoclientes = open("datos.txt","w")
                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                archivoclientes.close()
            elif op ==0:
                break
            else:
                os.system("cls")
                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘Error opcion no valida✘".center(120))
                sleep(2)
                os.system("cls")


while True:
    try:
        os.system("cls")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"COMO DESEA INGRESAR".center(97))
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\t\t\t\t\t\tMENU")
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╔═══════════════✧❂✧══════════════╗")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                         ")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t         1)Administrador                ")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t         2)Cliente                      ")
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                                       ")
        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╚════════════════✧♛✧═════════════╝")
        opcion = int((input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t⁃Dijite una opcion del menu ➣ ")))
        if opcion == 1:
            while True:
                os.system("cls")
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╔═══════════════✧❂✧══════════════╗")
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                         ")
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t          lOGIN ADMINISTRADOR     ")
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                                  ")
                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t                       0)Cancelar  ")
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╚════════════════✧♛✧═════════════╝")
                userad = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\t\t\t\t\t⁃Usuario ➣ ")
                if administrador == userad:
                    contraseña = stdiomask.getpass("\t\t\t\t\t⁃Contraseña ➣ ")
                    if contraseña == admcontra:
                        sleep(2)
                        os.system("cls")
                        barra_carga()
                        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"Bienvenido al sistema".center(120))
                        while True:
                            try:
                                os.system("cls")
                                init()
                                print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"╭───────────────────────────────────────────❀")
                                print("│Iniciaste como Administrador")
                                print("│en la cuentade",userad,)
                                print('''╰─────────────────────────────────────────❀''')
                                print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\n\t\t\t\t\t\tMENU")
                                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╔════════════════✧❂✧════════════════╗")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                         ")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     1)Agregar datos del Cliente  ")  
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     2)Mostrar datos de Cliente   ")  
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     3)Modificar datos de Cliente ")  
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     4)Eliminar datos de Cliente  ")  
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                                ")
                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\t\t\t0)   Salir                      ")  
                                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╚════════════════✧♛✧════════════════╝")
                                init()
                                opcion = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t⁃Dijite una opcion del menu ➣ "))
                                if opcion == 1:
                                    os.system("cls")
                                    print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"Nuevo registro de Cliente".center(120))
                                    pedirdatos()
                                elif opcion == 2:
                                    sleep(1)
                                    os.system("cls")
                                    mostrardatos()
                                elif opcion == 3:
                                    sleep(1)
                                    os.system("cls")
                                    init()
                                    print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\t\tModificar datos de cliente")
                                    editar()
                                elif opcion == 4:
                                    sleep(1)
                                    os.system("cls")
                                    init()
                                    print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\tEliminar datos de cliente")
                                    if open("datos.txt"):
                                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\tBorrando datos de Cliente")
                                        sleep(3)
                                        os.remove("datos.txt")
                                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\t\tDATOS BORRADOS!")
                                        sleep(2)
                                        os.system("cls")
                                elif opcion == 0:
                                    os.system("cls")
                                    print(Fore.LIGHTCYAN_EX+Style.BRIGHT+'''\n\n\n\n\t\t\t\t\t. . . . . . . . . ╰──╮ Gracias por utilizar Gicorp╭──╯ . . . . . . . . .
                                    \n\n\n\n''')
                                    sleep(2)
                                    os.system("cls")
                                    break
                                else:
                                    os.system("cls")
                                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"Opcion no valida".center(120))
                                    sleep(1)
                                    os.system("cls")
                            except ValueError:
                                os.system("cls")
                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\t\t\t\tSeleccione una opcion ")
                                sleep(2)
                    else:
                        os.system("cls")
                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"Contraseña incorrecta".center(120))
                        sleep(2)
                        os.system("cls")
                elif userad =='0':
                    os.system("cls")
                    sleep(1)
                    break 
                else:
                    os.system("cls")
                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"Usuario no existe".center(120))
                    sleep(2)
                    os.system("cls")               
        elif opcion == 2:
            while True:
                os.system("cls")
                init()
                archivoclientes= open("datos.txt","r")
                datosCuenta= archivoclientes.readline().strip().split(",")
                numeroCuenta= datosCuenta[0]
                nonmbreCuenta = datosCuenta[1]
                contraCuenta = datosCuenta[2]
                saldo =  int(datosCuenta[3])
                nonmbrecliente= datosCuenta[4]
                cuidacliente = datosCuenta[5]
                cellcliente = datosCuenta[6]
                correocliente =datosCuenta[7]
                edadcliente = datosCuenta[8]
                archivoclientes.close()
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╔═══════════════✧❂✧══════════════╗")
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                         ")
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t            lOGIN CLIENTE               ")
                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                                  ")
                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t                       0)Cancelar  ")
                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╚════════════════✧♛✧═════════════╝")
                usercliente = input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\t\t\t\t\t⁃Usuario ➣ ")
                if usercliente == nonmbreCuenta:
                    contracliente = stdiomask.getpass(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t\t⁃Contraseña ➣ ")
                    if  contracliente == contraCuenta and usercliente == nonmbreCuenta and contracliente == contraCuenta:
                        sleep(1)
                        os.system("cls")
                        barra_carga()
                        while True:
                            try:
                                os.system("cls")
                                print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"╭─────────────────────❀")
                                print("│Bienvenido",nonmbreCuenta)
                                print('''╰─────────────────────❀''')
                                print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\n\t\t\t\t\t\tMENU ")
                                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\n\t\t\t\t╔════════════════✧❂✧════════════════╗")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                         ")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     1)Ingresar dinero en la cuenta ")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     2)Retirar  dinero de la cuenta ")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t     3)Mostrar  dinero disponible   ")
                                print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t                         ")
                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\t\t\t      0)Salir                        ")
                                print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╚═════════════════✧♛✧════════════════╝")
                                init()
                                opcion = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t⁃Dijite una opcion del menu ➣ "))
                                if opcion == 1:
                                    while True:
                                        try:
                                            fechaActual = datetime.datetime.now()
                                            fechaActual2 = datetime.datetime.strftime(fechaActual,"%d/%m/%Y %H:%M:%S")
                                            os.system("cls")
                                            extra = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\t⁃Cuanto dinero desea ingresar ➣ "))
                                            if  extra <0:
                                                os.system("cls")
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\tMonto no valido")
                                                sleep(2)
                                                os.system("cls")
                                            else:
                                                os.system("cls")
                                                saldo += extra
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                *********************************
                                                                GiCorp
                                                *********************************''')
                                                print(" \t\t\t\t\t       DEPOCITO CTA AHORROS   ")
                                                print(" \t\t\t\t     FECHA         :",fechaActual2        )   
                                                print(" \t\t\t\t     DEPOCITO DE   : USD" ,extra          )
                                                print(" \t\t\t\t     USUARIO       :",nonmbreCuenta       )
                                                print(" \t\t\t\t     SALDO NUEVO   : USD" ,saldo          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                break
                                        except ValueError:
                                            os.system("cls")                             
                                            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\n\t\t\t\t\tValor no valido")
                                            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tIngrese un valor entero")
                                            os.system("pause")
                                            os.system("cls")                             
                                elif opcion == 2:
                                    while True:
                                        os.system("cls")
                                        print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\n\t\t\t\t\t\tMENU DE RETIRO")
                                        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╔═════════════════════✧❂✧══════════════════════╗")
                                        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t│                                              │ ")
                                        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t│     1. $10                    5. $100        │")
                                        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t│     2. $20                    6. $200        │")
                                        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t│     3. $30                    7. $500        │")
                                        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t│     4. $50                    8. otro valor  │")
                                        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t│                                              │ ")
                                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t                                 0.Cancelar        ")
                                        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+"\t\t\t\t╚═════════════════════✧♛✧══════════════════════╝")
                                        
                                        opcion = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\t\t\t\t⁃Dijite una opcion del menu ➣ "))
                                        if opcion ==1:
                                            os.system("cls")
                                            retiro = 10
                                            if retiro > saldo: 
                                                barra_carga()
                                                print(Fore.RED+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo           )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==2:
                                            os.system("cls")
                                            retiro = 20
                                            if retiro > saldo: 
                                                barra_carga()
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo           )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")                                
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==3:
                                            os.system("cls")
                                            retiro = 30
                                            if retiro > saldo: 
                                                barra_carga()
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo          )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==4:
                                            retiro = 50
                                            os.system("cls")
                                            if retiro > saldo: 
                                                barra_carga()
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo     )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==5:
                                            retiro = 100
                                            os.system("cls")
                                            if retiro > saldo: 
                                                barra_carga()
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo           )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==6:
                                            retiro = 200
                                            os.system("cls")
                                            if retiro > saldo: 
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo           )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==7:
                                            retiro = 500
                                            os.system("cls")
                                            if retiro > saldo:
                                                barra_carga()
                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘No tiene esa cantidad de dinero✘".center(120))
                                                os.system("pause")
                                                os.system("cls")
                                            else:
                                                saldo -= retiro
                                                archivoclientes = open("datos.txt","w")
                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                archivoclientes.close()
                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                    *********************************
                                                                GiCorp
                                                    *********************************''')
                                                print(" \t\t\t\t     FECHA       :",fechaActual2)   
                                                print(" \t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                print(" \t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                print(" \t\t\t\t     *********************************  ")
                                                print(" \t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                print(" \t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                print(" \t\t\t\t     SALDO       : USD" ,saldo           )
                                                print(" \t\t\t\t     RETIRO      : USD" ,retiro          )
                                                print("\n\n\n")
                                                os.system("pause")
                                                os.system("cls")
                                        elif opcion ==8:
                                            while True:
                                                try:
                                                    os.system("cls")
                                                    fechaActual = datetime.datetime.now()
                                                    fechaActual2 = datetime.datetime.strftime(fechaActual,"%d/%m/%Y %H:%M:%S")
                                                    retirar = int(input(Fore.LIGHTCYAN_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\t⁃Cuanto dinero desea retirar ➣ "))
                                                    if retirar > 500:
                                                        os.system("cls") 
                                                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\tMonto máximo excedido")
                                                        sleep(2)
                                                    else:
                                                        if  retirar <0:
                                                            os.system("cls")
                                                            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\tMonto no valido")
                                                            sleep(2)
                                                            os.system("cls")
                                                        else:
                                                            if retirar > saldo:
                                                                os.system("cls")
                                                                barra_carga()
                                                                os.system("cls")
                                                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\t✘No tiene esa cantidad de dinero✘".center(120))
                                                                os.system("pause")
                                                                os.system("cls")
                                                            else:
                                                                saldo -= retirar
                                                                archivoclientes = open("datos.txt","w")
                                                                archivoclientes.write(f"{numeroCuenta},{nonmbreCuenta},{contraCuenta},{saldo},{nonmbrecliente},{cuidacliente},{cellcliente},{correocliente},{edadcliente}")
                                                                archivoclientes.close()
                                                                os.system("cls")
                                                                print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                                                    *********************************
                                                                                GiCorp
                                                                    *********************************''')
                                                                print(" \t\t\t\t\t     FECHA       :",fechaActual2)   
                                                                print(" \t\t\t\t\t     USUARIO     : ",nonmbreCuenta)
                                                                print(" \t\t\t\t\t     CAJERO      : INTEGRADOR           ")
                                                                print(" \t\t\t\t\t     *********************************  ")
                                                                print(" \t\t\t\t\t     Transaccion : RETIRO CTA AHORROS   ")
                                                                print(" \t\t\t\t\t     FEC.CONTABLE: ",fechaActual2        )
                                                                print(" \t\t\t\t\t     SALDO       : USD" ,saldo           )
                                                                print(" \t\t\t\t\t     RETIRO      : USD" ,retirar         )
                                                                print("\n\n\n")
                                                                os.system("pause")
                                                                os.system("cls")
                                                                break
                                                except ValueError:
                                                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tValor no valido")
                                                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tIngrese un valor entero")
                                                        os.system("pause")
                                                        os.system("cls")
                                        elif opcion ==0:
                                            os.system("cls")
                                            barra_carga()
                                            break
                                        else:
                                            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\t\t\t\t\tOpcion no valida")
                                            sleep(2)
                                            os.system("cls")
                                elif opcion == 3:
                                    fechaActual = datetime.datetime.now()
                                    fechaActual2 = datetime.datetime.strftime(fechaActual,"%d/%m/%Y %H:%M:%S")
                                    os.system("cls")
                                    print(Fore.LIGHTWHITE_EX+Style.BRIGHT+'''
                                    *********************************
                                                    GiCorp
                                    *********************************''')
                                    print(" \t\t\t         CONSULTA CTA AHORROS   ")
                                    print(" \t\t\t     FECHA   :",fechaActual2)   
                                    print(" \t\t\t     Usuario :",nonmbreCuenta)
                                    print(" \t\t\t     SALDO Disponible: " ,saldo           )
                                    print("\n\n\n")
                                    os.system("pause")
                                elif opcion == 0:
                                    os.system("cls")
                                    print("\n\n\n\n\t\t\t\t\t. . . . . .╰──╮ Gracias por utilizar Gicorp╭──╯ . . . . . . . . .")
                                    sleep(2)
                                    os.system("cls")
                                    break
                                else:
                                    os.system("cls")
                                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\t✘Error opcion no valida✘")
                                    sleep(2)
                                    os.system("cls")
                            except ValueError:
                                os.system("cls")
                                print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\t\tNingun Valor dijitado")
                                sleep(2)                        
                    else:
                        contador += 1
                        os.system("cls")
                        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\tcontraseña incorrecta")
                        print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+f"Numero de intentos:{contador}".center(120))
                        sleep(3)
                        os.system("cls")
                        if contador == 3:
                            print(Fore.LIGHTRED_EX+Style.BRIGHT+'''\n\n\n\n\n\t\t\t\t\tLimite de intentos alcanzado
                                        \n\t\t\t\t\tCuenta Bloqueada
                            ''')
                            sleep(2)
                            os.system("cls")
                            sys.exit() 
                elif usercliente =='0':
                    os.system("cls")
                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\Regresando a inicio")
                    break
                else:
                    os.system("cls")  
                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\n\t\t\t\t\tEl usuario no existe")
                    sleep(2)
                    os.system("cls")
        else:
            os.system("cls")
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"✘Error popcion no valida✘".center(120))
            sleep(2)
            os.system("cls")
            break

    except ValueError:
        os.system("cls")
        print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\n\n\n\t\t\t\t\t\tNingun Valor dijitado")
        sleep(2)
 
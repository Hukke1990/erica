import pacientes
import diagnosticos
import menuUsuario
from datetime import datetime
import platform
import os
import menuPacientes
from colorama import Fore


def limpiarPantalla():  # limpiar la consola completa
    sistema_operativo = platform.system()
    if sistema_operativo == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage


now = datetime.now()


class MenuGeneral:

    def main(self):
        limpiarPantalla()
        print(f'{Fore.CYAN}BIENVENIDOS A SU CONTROL DE PACIENTES{Fore.RESET}')
        print(f'Para poder utilizar esta aplicacion debe conectarse con su cuenta\n')
        print(f'1: Conectarse')
        print(f'2: Registrarse')

        while True:
            opcion = input(f'\n{Fore.YELLOW}Elija una opcion: {Fore.RESET}')

            if opcion == '1':
                menuUsuario.MenuUsuario.conectarse(self)
            elif opcion == '2':
                menuUsuario.MenuUsuario.registrarse(self)
            else:
                print(f'Opcion invalida!')

    def menuPrincipal(self, usuarioActual):
        while True:
            limpiarPantalla()
            '''print(current_date_format(now))
            print('{:->35}'.format(''))'''
            # OTRO METODO DE FECHA

            print(
                f'''{Fore.CYAN}Bienvenid@: {Fore.RESET}{usuarioActual['nombre_usuario'].capitalize()}           {current_date_format(now)}''')

            print(f"\n{Fore.CYAN}MENU PRINCIPAL{Fore.RESET}")
            print(f"1. Pacientes")
            print(f"2. Historial")

            opcion = input(f'\n{Fore.YELLOW}Elija una opcion: {Fore.RESET}')

            if opcion == "1":
                self.menuPacientes(usuarioActual)
            elif opcion == "2":
                self.menuHistorial(usuarioActual)
            else:
                print(f"{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}")

    def menuPacientes(self, usuarioActual):
        while True:
            limpiarPantalla()
            print(current_date_format(now))

            print(f"\n{Fore.CYAN}MENU PACIENTES{Fore.RESET}")
            print(f"1. Visualizar paciente")
            print(f"2. Registrar paciente")
            print(f"3. Buscar paciente")
            print(f"4. Realizar diagnostico")
            print(f"5. Historial clinico")
            print(f"6. Volver al menu principal")

            opcion = input(f'\n{Fore.YELLOW}Elija una opcion: {Fore.RESET}')

            if opcion == "1":
                menuPacientes.MenuPacientes.verPacientes()
            elif opcion == "2":
                menuPacientes.MenuPacientes.agregarPacientes()
            elif opcion == "3":
                menuPacientes.MenuPacientes.buscarPacientes(self)
            elif opcion == "4":
                diagnosticos.Diagnosticos.registrarDiagnostico()
            elif opcion == "5":
                diagnosticos.Diagnosticos.verHistorialClinico()
            elif opcion == "6":
                self.menuPrincipal(usuarioActual)
            else:
                print(f"{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}")

    def menuHistorial(self, usuarioActual):
        pass


if __name__ == "__main__":
    test = MenuGeneral()
    test.main()

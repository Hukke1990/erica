import pacientes
import tester
from colorama import Fore


class MenuPacientes:

    def verPacientes():
        tester.limpiarPantalla()
        print(f"{Fore.CYAN}VER PACIENTES{Fore.RESET}")
        pacientesLista = pacientes.Pacientes.verPacientes()
        for i, p in enumerate(pacientesLista, start=1):
            print(f'{i}: {Fore.GREEN}ID:{Fore.RESET}{p.obtenerIdPacientes()}, {Fore.GREEN}Nombre completo:{Fore.RESET} {p.obtenerNombre().capitalize()} {p.obtenerApellido().capitalize()}')
        return input(f'\nPrecione una tecla para continuar')

    def agregarPacientes():
        global pacientes
        tester.limpiarPantalla()
        print(f"{Fore.CYAN}MENU PACIENTES{Fore.RESET}")
        pacientes = pacientes.Pacientes(None, '', '', '', '', '', '', '', '')
        pacientes.establecerIdPacientes()
        nombre = input(f'{Fore.GREEN}Nombre: {Fore.RESET}')
        pacientes.establecerNombre(nombre)
        apellido = input(f'{Fore.GREEN}Apellido: {Fore.RESET}')
        pacientes.establecerApellido(apellido)
        cedula = input(f'{Fore.GREEN}Cedula: {Fore.RESET}')
        pacientes.establecerCedula(cedula)
        provincia = input(f'{Fore.GREEN}Provincia: {Fore.RESET}')
        pacientes.establecerProvincia(provincia)
        ciudad = input(f'{Fore.GREEN}Ciudad: {Fore.RESET}')
        pacientes.establecerCiudad(ciudad)
        direccion = input(f'{Fore.GREEN}Direccion: {Fore.RESET}')
        pacientes.establecerDireccion(direccion)
        while True:
            telefono = input(f'{Fore.GREEN}Telefono: {Fore.RESET}')
            if pacientes.establecerTelefono(telefono):
                while True:
                    correo = input(f'{Fore.GREEN}Correo: {Fore.RESET}')
                    if pacientes.establecerCorreo(correo):
                        opcion = input(
                            f'\n{Fore.YELLOW}Desea registrar este paciente?[S/N]: {Fore.RESET}').lower()
                        if opcion == 's':
                            pacientes.agregarPacienteCompleto(pacientes.obtenerNombre(),
                                                              pacientes.obtenerApellido(),
                                                              pacientes.obtenerCedula(),
                                                              pacientes.obtenerProvincia(),
                                                              pacientes.obtenerCiudad(),
                                                              pacientes.obtenerDireccion(),
                                                              pacientes.obtenerTelefono(),
                                                              pacientes.obtenerCorreo())
                            print(f'''\n{Fore.YELLOW}Seleccione una opcion:
                                                                            1. Registrar otro paciente
                                                                            2. Finalizar la carga de datos{Fore.RESET}''')

                            volverACargar = input(f'>> ').lower()
                            if volverACargar == '1':
                                MenuPacientes.agregarPacientes()
                            elif volverACargar == '2':
                                return
                            else:
                                print(
                                    f'\n{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}')
                                continue
                        elif opcion == 'n':
                            print(
                                f'\n{Fore.RED}Ha cancelado la carga del paciente.{Fore.RESET}')
                            return
                        else:
                            print(
                                f'\n{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}')
                    else:
                        print(
                            f'\n{Fore.RED}Por favor ingrese un correo valido!{Fore.RESET}')
            else:
                print(
                    f'\n{Fore.RED}Por favor ingrese un telefono valido!{Fore.RESET}')
                continue

    def buscarPacientes(self):  # AGREGAR EL SELF AL METODO
        pacientesBuscar = []

        buscarPaciente = pacientes.Pacientes.buscarPacientes(self)
        if buscarPaciente is not None:
            pacientesBuscar.append(buscarPaciente)

        tester.limpiarPantalla()
        print(f"{Fore.CYAN}PACIENTE ENCONTRADO{Fore.RESET}")
        print('{:->35}'.format(''))  # agrega 35 lineas

        for p in pacientesBuscar:
            atributos = ["ID", "Nombre", "Apellido", "Cedula",
                         "Provincia", "Ciudad", "Direccion", "Telefono", "Correo"]

        metodos = [p.obtenerIdPacientes, p.obtenerNombre, p.obtenerApellido, p.obtenerCedula,
                   p.obtenerProvincia, p.obtenerCiudad, p.obtenerDireccion, p.obtenerTelefono, p.obtenerCorreo]

        for atributo, metodo in zip(atributos, metodos):
            try:
                print(f"{Fore.GREEN}{atributo}: {Fore.RESET}{metodo()}")
            except TypeError:
                print(
                    f"{Fore.RED}Error: {metodo} no es un metodo valido!{Fore.RESET}")

        opcion = input(
            f'\n{Fore.YELLOW}Desea editar el paciente?[S/N]: {Fore.RESET}').lower()

        if opcion == 's':
            MenuPacientes.editarPacientes(self, pacientesBuscar)
        elif opcion == 'n':
            return
        else:
            print(
                f'\n{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}')

    def editarPacientes(self, pacientesBuscar):
        camposModificados = []

        while True:
            tester.limpiarPantalla()
            print(f"{Fore.CYAN}EDITAR PACIENTE{Fore.RESET}")
            print('{:->35}'.format(''))  # agrega 35 lineas

            for p in pacientesBuscar:
                atributos = ["ID", "Nombre", "Apellido", "Cedula",
                             "Provincia", "Ciudad", "Direccion", "Telefono", "Correo"]

            metodos = [p.obtenerIdPacientes, p.obtenerNombre, p.obtenerApellido, p.obtenerCedula,
                       p.obtenerProvincia, p.obtenerCiudad, p.obtenerDireccion, p.obtenerTelefono, p.obtenerCorreo]

            for atributo, metodo in zip(atributos, metodos):
                if atributo in camposModificados:
                    print(f"{Fore.CYAN}{atributo}: {Fore.RESET}{metodo()}")
                else:
                    print(f"{Fore.GREEN}{atributo}: {Fore.RESET}{metodo()}")
            print('\n')

            opcionEdicion = {
                1: 'Editar Nombre',
                2: 'Editar Apellido',
                3: 'Editar Cedula',
                4: 'Editar Provincia',
                5: 'Editar Ciudad',
                6: 'Editar Direccion',
                7: 'Editar Telefono',
                8: 'Editar Correo',
                9: 'Guardar Cambios',
                10: 'Borrar Paciente',
                11: 'Volver al menu principal'
            }

            for opcion, mensaje in opcionEdicion.items():
                print(f'{Fore.YELLOW}{opcion}. {mensaje}{Fore.RESET}')

            try:
                opcion = int(
                    input(f'\n{Fore.YELLOW}Ingrese la opcion deseada: {Fore.RESET}'))
            except ValueError:
                print(
                    f'\n{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}')
                continue

            if opcion == 1:
                nuevoNombre = input(
                    f'Nuevo nombre, "c" para cancelar: ').lower()
                if nuevoNombre == 'c':
                    continue
                else:
                    p.establecerNombre(nuevoNombre)
                    camposModificados.append('Nombre')

            elif opcion == 2:
                nuevoApellido = input(
                    f'Nuevo apellido, "c" para cancelar: ').lower()
                if nuevoApellido == 'c':
                    continue
                else:
                    p.establecerApellido(nuevoApellido)
                    camposModificados.append('Apellido')

            elif opcion == 3:
                nuevoCedula = input(
                    f'Nueva cedula, "c" para cancelar: ').lower()
                if nuevoCedula == 'c':
                    continue
                else:
                    p.establecerCedula(nuevoCedula)
                    camposModificados.append('Cedula')

            elif opcion == 4:
                nuevaProvincia = input(
                    f'Nueva provincia, "c" para cancelar: ').lower()
                if nuevaProvincia == 'c':
                    continue
                else:
                    p.establecerProvincia(nuevaProvincia)
                    camposModificados.append('Provincia')

            elif opcion == 5:
                nuevaCiudad = input(
                    f'Nueva ciudad, "c" para cancelar: ').lower()
                if nuevaCiudad == 'c':
                    continue
                else:
                    p.establecerCiudad(nuevaCiudad)
                    camposModificados.append('Ciudad')

            elif opcion == 6:
                nuevaDireccion = input(
                    f'Nueva direccion, "c" para cancelar: ').lower()
                if nuevaDireccion == 'c':
                    continue
                else:
                    p.establecerDireccion(nuevaDireccion)
                    camposModificados.append('Direccion')

            elif opcion == 7:
                nuevoTelefono = input(
                    f'Nuevo telefono, "c" para cancelar: ').lower()
                if nuevoTelefono == 'c':
                    continue
                else:
                    p.establecerTelefono(nuevoTelefono)
                    camposModificados.append('Telefono')

            elif opcion == 8:
                nuevoCorreo = input(
                    f'Nuevo correo, "c" para cancelar: ').lower()
                if nuevoCorreo == 'c':
                    continue
                else:
                    p.establecerCorreo(nuevoCorreo)
                    camposModificados.append('Correo')

            elif opcion == 9:
                pacientes.Pacientes.editarPacientes(p)
                print(
                    f'\n{Fore.GREEN}Paciente actualizado con exito!{Fore.RESET}')
                input(f'Precione una tecla para continuar')

            elif opcion == 10:
                pacientes.Pacientes.eliminarPacientes(p)
                print(
                    f'\n{Fore.GREEN}Paciente eliminado con exito!{Fore.RESET}')
                int(f'Precione una tecla para continuar')

            elif opcion == 11:
                break

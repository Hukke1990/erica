import json
import os
from datetime import datetime
from colorama import Fore
import pacientes
import random
import tester


class Diagnosticos:

    @staticmethod
    def registrarDiagnostico():
        tester.limpiarPantalla()
        pacienteObj = pacientes.Pacientes(None, "", "", "", "", "", "", "", "")
        pacienteSeleccionado = pacienteObj.buscarPacientes()

        if not pacienteSeleccionado:
            return

        print(f'\n{Fore.CYAN}Datos del paciente seleccionado: {Fore.RESET}')
        print(f'Nombre: {pacienteSeleccionado.obtenerNombre().capitalize()}')
        print(
            f'Apellido: {pacienteSeleccionado.obtenerApellido().capitalize()}')
        print(f'Cédula: {pacienteSeleccionado.obtenerDNI()}')

        diagnostico = input("Ingrese el diagnóstico del paciente: ")
        comentarios = input('Comentarios (opcional): ') or None
        fecha = datetime.now().strftime("%d/%m/%Y")

        nuevo_diagnostico = {
            "idDiagnostico": 'DIAG' + str(random.randint(1000, 9999)),
            "idPacientes": pacienteSeleccionado.obtenerIdPacientes(),
            "nombre": pacienteSeleccionado.obtenerNombre(),
            "apellido": pacienteSeleccionado.obtenerApellido(),
            "DNI": pacienteSeleccionado.obtenerDNI(),
            "diagnostico": diagnostico,
            "comentarios": comentarios,
            "fecha": fecha
        }

        dataDiagnosticos = Diagnosticos.cargarJson()
        dataDiagnosticos["diagnosticos"].append(nuevo_diagnostico)
        Diagnosticos.guardarJson(dataDiagnosticos)

        print(f'{Fore.GREEN}Diagnóstico registrado con éxito!{Fore.RESET}')
        input(f'{Fore.CYAN}Presione enter para continuar...{Fore.RESET}')

    @staticmethod
    def verHistorialClinico():
        pacienteObj = pacientes.Pacientes(None, "", "", "", "", "", "", "", "")
        pacienteSeleccionado = pacienteObj.buscarPacientes()

        if not pacienteSeleccionado:
            return

        dataDiagnosticos = Diagnosticos.cargarJson()
        historial = [
            d for d in dataDiagnosticos["diagnosticos"]
            if d["idPacientes"] == pacienteSeleccionado.obtenerIdPacientes()
        ]

        if historial:
            tester.limpiarPantalla()
            print(f'{Fore.CYAN}HISTORIAL CLINICO{Fore.RESET}')

            print(f'\n{Fore.CYAN}Paciente:{Fore.RESET} {pacienteSeleccionado.obtenerNombre().capitalize()} {pacienteSeleccionado.obtenerApellido().capitalize()}')
            print(f'\n')
            for entry in historial:
                print(
                    f'{Fore.GREEN}Fecha:{Fore.RESET} {entry["fecha"]} - {Fore.GREEN}Diagnóstico:{Fore.RESET} {entry["diagnostico"]} ({entry["comentarios"]})')
            input(
                f'\n{Fore.YELLOW}Presione enter para continuar...{Fore.RESET}')
        else:
            print(
                f'{Fore.RED}El paciente no tiene diagnósticos registrados!{Fore.RESET}')

    # MANEJO DE ARCHIVO JSON
    @staticmethod
    def cargarJson():
        if os.path.exists('diagnosticos.json') and os.path.getsize('diagnosticos.json') > 0:
            with open('diagnosticos.json', 'r') as archivoDiagnosticos:
                dataDiagnosticos = json.load(archivoDiagnosticos)
                return dataDiagnosticos
        else:
            return {"diagnosticos": []}

    @staticmethod
    def guardarJson(dataDiagnosticos):
        with open('diagnosticos.json', 'w') as archivoDiagnosticos:
            json.dump(dataDiagnosticos, archivoDiagnosticos, indent=4)

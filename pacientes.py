import json
import random
import os
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from colorama import Fore
from difflib import get_close_matches
import tester

# AGREGAR OBRA SOCIAL
# AGREGAR FECHA NACIMIENTO


class Pacientes:

    def __init__(self, idPacientes, nombre, apellido, DNI, obraSocial, provincia, ciudad, direccion, telefono, correo):
        self.__idPacientes = idPacientes
        self.__nombre = nombre
        self.__apellido = apellido
        self.__DNI = DNI
        self.__obraSocial = obraSocial
        self.__provincia = provincia
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo

    # Setters
    def establecerIdPacientes(self):
        self.__idPacientes = 'PAC' + str(random.randint(1000, 9999))
        return self.__idPacientes

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def establecerApellido(self, apellido):
        self.__apellido = apellido

    def establecerDNI(self, DNI):
        self.__DNI = DNI

    def establecerObraSocial(self, obraSocial):
        self.__obraSocial = obraSocial

    def establecerProvincia(self, provincia):
        self.__provincia = provincia

    def establecerCiudad(self, ciudad):
        self.__ciudad = ciudad

    def establecerDireccion(self, direccion):
        self.__direccion = direccion

    def establecerTelefono(self, telefono):
        try:
            numero = phonenumbers.parse(telefono, None)
            if phonenumbers.is_valid_number(numero):
                self.__telefono = telefono
                return True
            else:
                return False
        except phonenumbers.phonenumberutil.NumberParseException:
            return False

    def establecerCorreo(self, correo):
        try:
            validate_email(correo)
            self.__correo = correo
            return True
        except EmailNotValidError:
            return False

    def agregarPacienteCompleto(self, nombre, apellido, DNI, obraSocial, provincia, ciudad, direccion, telefono, correo):
        dataPacientes = {'pacientes': []}

        if os.path.exists('pacientes.json') and os.path.getsize('pacientes.json') > 0:
            dataPacientes = Pacientes.cargarJson()

        if not nombre or not apellido or not DNI or not obraSocial or not provincia or not ciudad or not direccion or not telefono or not correo:
            return False

        pacienteExiste = any(p["nombre"] == nombre.lower() and
                             p["apellido"] == apellido.lower() and
                             p["DNI"] == DNI.lower() and
                             p["obraSocial"] == obraSocial.lower() and
                             p["provincia"] == provincia.lower() and
                             p["ciudad"] == ciudad.lower() and
                             p["direccion"] == direccion.lower() and
                             p["telefono"] == telefono.lower() and
                             p["correo"] == correo.lower() for p in dataPacientes["pacientes"])
        if pacienteExiste:
            print(f'{Fore.RED}El paciente ya se encuentra registrado!{Fore.RESET}')
            return

        dataPacientes["pacientes"].append({"idPacientes": self.obtenerIdPacientes(),
                                           "nombre": nombre.lower(),
                                           "apellido": apellido.lower(),
                                           "DNI": DNI.lower(),
                                           "obraSocial": obraSocial.lower(),
                                           "provincia": provincia.lower(),
                                           "ciudad": ciudad.lower(),
                                           "direccion": direccion.lower(),
                                           "telefono": telefono.lower(),
                                           "correo": correo.lower()
                                           })

        Pacientes.guardarJson(dataPacientes)
        print(f'{Fore.GREEN}Paciente registrado con exito!{Fore.RESET}')

    def buscarPacientes(self):  # AGREGAR EL SELF DE PACIENTES
        tester.limpiarPantalla()
        print(f"{Fore.CYAN}BUSCAR PACIENTES{Fore.RESET}")
        dataPacientes = Pacientes.cargarJson()

        buscarPaciente = input(
            f'{Fore.YELLOW}Ingrese apellido del paciente, "0" para regresar: {Fore.RESET}').lower()
        if buscarPaciente == '0':
            return

        buscar = buscarPaciente.lower()

        pacientesEncontrados = []

        for paciente in dataPacientes["pacientes"]:
            buscarApellidoPaciente = paciente["apellido"].lower()
            similitud = get_close_matches(
                buscar, [buscarApellidoPaciente], n=1, cutoff=0.6)

            if similitud:
                pacientesEncontrados.append(paciente)

        if not pacientesEncontrados:
            print(f'{Fore.RED}No se encontraron coincidencias!{Fore.RESET}')
            return

        tester.limpiarPantalla()
        print(f'{Fore.CYAN}PACIENTES ENCONTRADOS: {Fore.RESET}')
        for idx, paciente in enumerate(pacientesEncontrados, start=1):
            print(
                f'{Fore.GREEN}{idx}. Nombre completo:{Fore.RESET} {paciente["apellido"].capitalize()} {paciente["nombre"].capitalize()} - {Fore.GREEN}DNI:{Fore.RESET} {paciente["DNI"]}')

        while True:
            try:
                elegirIdx = int(
                    input(f'\n{Fore.YELLOW}Elija una opcion: {Fore.RESET}')) - 1
                if 0 <= elegirIdx < len(pacientesEncontrados):
                    pacientesSeleccionado = pacientesEncontrados[elegirIdx]
                    paciente = Pacientes(pacientesSeleccionado["idPacientes"],
                                         pacientesSeleccionado["nombre"],
                                         pacientesSeleccionado["apellido"],
                                         pacientesSeleccionado["DNI"],
                                         pacientesSeleccionado["obraSocial"],
                                         pacientesSeleccionado["provincia"],
                                         pacientesSeleccionado["ciudad"],
                                         pacientesSeleccionado["direccion"],
                                         pacientesSeleccionado["telefono"],
                                         pacientesSeleccionado["correo"])
                    return paciente
                else:
                    print(
                        f'{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}')
            except ValueError:
                print(
                    f'{Fore.RED}Por favor ingrese una opcion valida!{Fore.RESET}')

    def editarPacientes(self):
        dataPaciente = Pacientes.cargarJson()

        for i, paciente in enumerate(dataPaciente["pacientes"]):
            if paciente["idPacientes"] == self.obtenerIdPacientes():
                dataPaciente['pacientes'][i] = self.toDict()
                break

        Pacientes.guardarJson(dataPaciente)

    def eliminarPacientes(self):
        dataPacientes = Pacientes.cargarJson()

        pacienteAEliminar = None
        for paciente in dataPacientes["pacientes"]:
            if paciente["idPacientes"] == self.obtenerIdPacientes():
                pacienteAEliminar = paciente
                break

        if pacienteAEliminar is not None:
            dataPacientes["pacientes"].remove(pacienteAEliminar)

        Pacientes.guardarJson(dataPacientes)

    # Getters
    def obtenerIdPacientes(self):
        return self.__idPacientes

    def obtenerNombre(self):
        return self.__nombre

    def obtenerApellido(self):
        return self.__apellido

    def obtenerDNI(self):
        return self.__DNI

    def obtenerObraSocial(self):
        return self.__obraSocial

    def obtenerProvincia(self):
        return self.__provincia

    def obtenerCiudad(self):
        return self.__ciudad

    def obtenerDireccion(self):
        return self.__direccion

    def obtenerTelefono(self):
        return self.__telefono

    def obtenerCorreo(self):
        return self.__correo

    def verPacientes():
        dataPacientes = Pacientes.cargarJson()

        pacientesLista = []

        for paciente in dataPacientes["pacientes"]:
            paciente = Pacientes(paciente["idPacientes"],
                                 paciente["nombre"],
                                 paciente["apellido"],
                                 paciente["DNI"],
                                 paciente["obraSocial"],
                                 paciente["provincia"],
                                 paciente["ciudad"],
                                 paciente["direccion"],
                                 paciente["telefono"],
                                 paciente["correo"])
            pacientesLista.append(paciente)

        return pacientesLista

    def __str__(self):
        return f'''
        ID: {self.obtenerIdPacientes()}
        Nombre: {self.obtenerNombre()}
        Apellido: {self.obtenerApellido()}
        DNI: {self.obtenerDNI()}
        Obra Social: {self.obtenerObraSocial()}
        Provincia: {self.obtenerProvincia()}
        Ciudad: {self.obtenerCiudad()}
        Direccion: {self.obtenerDireccion()}
        Telefono: {self.obtenerTelefono()}
        Correo: {self.obtenerCorreo()}
        '''

    # MANEJO ARCHIVO JSON
    @staticmethod
    def cargarJson():
        with open('pacientes.json', 'r') as archivoPacientes:
            dataPacientes = json.load(archivoPacientes)
            return dataPacientes

    @staticmethod
    def guardarJson(dataPacientes):
        with open('pacientes.json', 'w') as archivoPacientes:
            json.dump(dataPacientes, archivoPacientes, indent=4)

    def toDict(self):
        return {
            'idPacientes': self.obtenerIdPacientes(),
            'nombre': self.obtenerNombre(),
            'apellido': self.obtenerApellido(),
            'DNI': self.obtenerDNI(),
            'obraSocial': self.obtenerObraSocial(),
            'provincia': self.obtenerProvincia(),
            'ciudad': self.obtenerCiudad(),
            'direccion': self.obtenerDireccion(),
            'telefono': self.obtenerTelefono(),
            'correo': self.obtenerCorreo()
        }

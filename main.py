from vehiculo import Vehiculo
from mantencion import Mantencion
from fecha import Fecha

def buscarMarca(lista):
    marca = input("\nIngrese la marca del vehiculo: ").lower().title()
    encontrado = False
    for a in lista:
            if marca == a.marca:
                print("\n========================================\n")
                print(a.mostrarVehiculo())
                print("========================================")
                encontrado = True
    if not encontrado:
        print("\n========================================")
        print("\nNo se ha encontrado un vehiculos de esa marca \n")
        print("========================================")
    
def buscarPersona(lista):
    nomCliente = input("\nIngrese la persona que desea buscar (Nombre, Apellido): ").lower().title()
    encontrado = False
    for a in lista:
        if nomCliente == a.nomCliente:
            print("\n========================================\n")
            print(a.mostrarVehiculo())
            print("========================================")
            encontrado = True
    if not encontrado:
        print("\nNo hay vehiculos asignados a esa persona")
        print("\n========================================")

def menuVehiculo(lista):
    while True:
        try:
            print("\n========================================")
            opcion = int(input("\nDesea buscar por: \n\n1.Buscar por marca \n2.Buscar por persona \n3.Volver al menu \n\nIngrese la opcion (1 a 3): "))
            if opcion >= 1 and opcion <= 3:
                        if opcion == 1:
                            buscarMarca(lista)
                        elif opcion == 2:
                            buscarPersona(lista)
                        else:
                            print("\n========================================")
                            break
            else:
                print("\nOpcion fuera de rango. Intente nuevamente")
                print("\n========================================")
        except:
            print("\nIngrese solo opciones validas")
            print("\n========================================")

def agregarVehiculo():
    print("\n========================================")
    id = int(input("\nIngrese la ID del propietario: "))
    nomCliente = input("Ingrese el Nombre del Propietario (Nombre, Apellido): ").title()
    marca = input("Ingrese la marca del vehículo: ").title()
    modelo = input("Ingrese el modelo del vehículo: ").title()
    año = int(input("Ingrese el año del vehículo: "))
    nuevo_vehiculo = Vehiculo(id, nomCliente, marca, modelo, año, Mantencion("",Fecha(0,0,0))) 
    print("\nVehículo agregado con éxito.")
    print("\n========================================")
    return nuevo_vehiculo

def agregarMantencion(lista):
    print("\n========================================\n")
    vehiculo_id = int(input("Ingrese la ID del propietario: "))
    for vehiculo in lista:
        if vehiculo.id == vehiculo_id:
            nombre_mantencion = input("Ingrese descripcion de la mantencion: ").capitalize()
            dia = int(input("Ingrese el día de la mantención: "))
            mes = int(input("Ingrese el mes de la mantención: "))
            año = int(input("Ingrese el año de la mantención: "))
            nueva_mantencion = Mantencion(nombre_mantencion, Fecha(dia, mes, año))
            vehiculo.agregarMantencion(nueva_mantencion)
            print("\nMantención agregada con éxito al vehículo.")
            print("\n========================================")
            return lista
    print("\nNo se encontró un vehículo con ese ID asignada")
    print("\n========================================")
    return lista

#LISTAS
lista = []
c = Vehiculo(1,"Lucas Gonzalez","Toyota" ,"Corolla",2020 , Mantencion ("Cambio de Aceite", Fecha(20,3,2023)))
lista.append(c)
c = Vehiculo(2,"Pedro Rodriguez","Nissan","Sentra",2017, Mantencion ("Cambio de Bateria", Fecha(11,4,2019)))
lista.append(c)
c = Vehiculo(3,"Yasmin Gonzalez","Ford","Focus", 2019, Mantencion ("Cambio de Neumaticos", Fecha(20,6,2024)))
lista.append(c)
c = Vehiculo(4,"Maria Lopez","Honda","Civic", 2021, Mantencion ("Chequeo de luces", Fecha(20,6,2022)))
lista.append(c)
c = Vehiculo(5,"Pedro Rodriguez" ,"Audi","Audi Q7", 2017, Mantencion ("Cambio de Frenos", Fecha(18,7,2018)))
lista.append(c)

def leerOpcion():
    while True:
        try:
            opcion = int(input("\nIngresa una opción (1 a 4): "))
            if opcion < 1 or opcion > 4:
                print("Opción no válida") 
            else:
                return opcion
        except:
            print("\nDebes ingresar solo números")

def MenuOpciones():
    print("\nBienvenido al taller 'Mi Cacharrito'\n \nQue desea realizar\n \n1.Buscar Vehiculos \n2.Agregar Nuevo Vehiculo \n3.Agregar Nueva Mantencion \n4.Salir")

#PP
while True:
    MenuOpciones()
    opcion = leerOpcion()
    if opcion == 4:
        print("\nAdiós, ¡Vuelva Pronto!")
        break
    elif opcion == 1:
        menuVehiculo(lista)
    elif opcion == 2:
        nuevo_vehiculo =agregarVehiculo()
        lista.append(nuevo_vehiculo)
    elif opcion == 3:
        lista = agregarMantencion(lista)

# Nicolás Barrios
# Lucas Gonzalez
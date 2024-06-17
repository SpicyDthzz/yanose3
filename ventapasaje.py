import os 
os.system ("cls")

totalRecaudado = 0
totalPasajesVendidos = 0
seguir = "s"

while seguir == "s" or seguir == "S":
    print("Bienvenido a TarBas: que desea hacer?")
    print("1. Comprar pasajes")
    print("2. Estadisticas de venta")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        print("Destinos disponibles:")
        print("1. Temuco")
        print("2. Curico")
        print("3. Puerto Montt")
        destino = input("Seleccione un destino: ")
        
        if destino == "1":
            print("Ha seleccionado Temuco")
        elif destino == "2":
            print("Ha seleccionado Curico")
        elif destino == "3":
            print("Ha seleccionado Puerto Montt")
        
        print("Tipos de pasajes:")
        print("1. Solo Ida")
        print("2. Ida y Vuelta")
        tipoPasaje = input("Seleccione un tipo de pasaje: ")
        
        if tipoPasaje == "1":
            if destino == "1":
                precioUnitario = 10000
            elif destino == "2":
                precioUnitario = 18000
            elif destino == "3":
                precioUnitario = 25000
        elif tipoPasaje == "2":
            if destino == "1":
                precioUnitario = 18000
            elif destino == "2":
                precioUnitario = 30000
            elif destino == "3":
                precioUnitario = 40000
            descuento = precioUnitario * 0.1
            totalConDescuento = precioUnitario - descuento
        
        cantidadPasajes = int(input("Ingrese la cantidad de pasajes a comprar: "))
        
        totalVenta = cantidadPasajes * precioUnitario
        totalRecaudado += totalVenta
        totalPasajesVendidos += cantidadPasajes
        
        print("El total a pagar es:", totalVenta)
        
        print("Imprimiendo ticket...")
        print("-----------------------------------------")
        print("         Ticket de compra")
        print("-----------------------------------------")
        print("Origen - Destino:", destino)
        if tipoPasaje == "1":
            print("Tipo de pasaje: Solo Ida")
        elif tipoPasaje == "2":
            print("Tipo de pasaje: Ida y Vuelta")
            print("Descuento aplicado:", descuento)
            print("Total con descuento:", totalConDescuento)
        print("Cantidad de pasajes:", cantidadPasajes)
        print("Total a pagar:", totalVenta)
        print("-----------------------------------------")
    
    elif opcion == "2":
        print("Estadisticas:")
        print("Total recaudado:", totalRecaudado)
        print("Total pasajes vendidos:", totalPasajesVendidos)
    
    elif opcion == "3":
        print("Saliendo del programa...")
        seguir = "n"
    
    else:
        print("Opcion no valida")

print("Fin del programa")
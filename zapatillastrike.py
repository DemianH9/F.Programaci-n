# Programa de reservas para la tienda "Zapatillas Strike"

reservas = {}  # Diccionario: nombre -> cantidad de pares reservados
stock_maximo = 20

def reservar_zapatillas():
    global reservas
    print("\n-- Reservar Zapatillas --")
    nombre = input("Nombre del comprador: ").strip()

    if nombre in reservas:
        print("Error: El comprador ya tiene una reserva.")
        return

    if len(reservas) >= stock_maximo:
        print("Error: No hay más stock disponible.")
        return

    clave = input("Digite la palabra secreta para confirmar la reserva: ")
    if clave != "EstoyEnListaDeReserva": #porfavor ingrese exactamnete como esta puesto 
        print("Error: palabra clave incorrecta. Reserva no realizada.")
        return

    reservas[nombre] = 1
    print(f"Reserva realizada exitosamente para {nombre}.")

def buscar_reserva():
    global reservas
    print("\n-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ").strip()

    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return

    cantidad = reservas[nombre]
    tipo = "VIP" if cantidad == 2 else "estándar"
    print(f"Reserva encontrada: {nombre} - {cantidad} par(es) ({tipo}).")

    if cantidad == 1:
        decision = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
        if decision == "s":
            if total_reservas() + 1 > stock_maximo:
                print("No se puede actualizar a VIP. No hay suficiente stock.")
            else:
                reservas[nombre] = 2
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
        else:
            print("Manteniendo reserva actual.")

def ver_stock():
    print("\n-- Ver Stock de Reservas --")
    reservados = total_reservas()
    disponibles = stock_maximo - reservados
    print(f"Pares reservados: {reservados}")
    print(f"Pares disponibles: {disponibles}")

def total_reservas():
    return sum(reservas.values())

def menu():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Ver stock de reservas")
        print("4.- Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            reservar_zapatillas()
        elif opcion == "2":
            buscar_reserva()
        elif opcion == "3":
            ver_stock()
        elif opcion == "4":
            print("\nPrograma terminado...")
            break
        else:
            print("\nDebe ingresar una opción válida!!")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
                    }
#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                }

def stock_marca(marca):
    total_stock = 0
    marca = marca.lower()
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            total_stock += stock[modelo][1]
            print(f"El stock es: {total_stock}, modelo: {modelo}")

def búsqueda_ram_precio(ram_min, ram_max, precio):
    encontrados = False 
    for modelo, datos in productos.items():
        try:
            if modelo in stock and stock[modelo][1]>0:
                ram_num = int(datos[2].replace("GB", ""))
                if ram_min <= ram_num <= ram_max and stock[modelo][0] <= precio:
                    print (datos)
                    encontrados = True
        except:
            continue
        if not encontrados: 
            print("No hay notebooks que mostrar")

def eliminar_productos(modelo): 
    if modelo in productos and modelo in stock:
        del productos[modelo]
        del stock[modelo]
        return True
    return False


def menu():
    while True:
        print("\n***MENU***")
        print("1.- Stock marca")
        print("2.- Búsqueda por RAM")
        print("3.- Eliminar producto")
        print("4.- Salir")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                marca = input("Ingrese marca a buscar: ")
                stock_marca(marca)
            elif opcion == 2:
                while True:
                    try:
                        ram_min = int(input("Ingrese la ram minima que busca:"))
                        ram_max = int(input("Ingrese la ram maxima que busca:"))
                        precio = int(input("Ingrese la ram minima que busca:"))
                        búsqueda_ram_precio(ram_min,ram_max,precio)
                        break
                    except:
                        print("Debes ingresar valores enteros!!")
            elif opcion == 3:
                while True:
                    modelo = input("Ingrese un modeloa eliminar:")
                    if eliminar_productos(modelo):
                        print("Producto eliminado")
                    else:
                        print("El producto no existe!")
                    continuar = input("deseas eliminar otro producto? si/no").lower()
                    if continuar != "si":
                        break              
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("Debe ingresar un número.")
if __name__ == "__main__":
    menu()

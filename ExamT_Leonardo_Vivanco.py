productos = {'modelo': ['marca', 'pantalla', 'RAM', 'disco', 'GB de DD', 'procesador', 'video']}
stock = {"modelo": ["precio", "stock"]}
roductos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
            }.upper()
stock = {'8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
 'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
 'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
        }.upper()

def stock_marca():
    marca=input("Ingrese la marca que desea saber su stock: ").upper()
    if marca in productos:
        print(f"Stock: {stock["modelo"][1]}")
    else:
        print("Stock: 0")


def menu():
    while True:
        print("***MENÚ PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        op=input("Ingrese una opción: ")
        if op=="1":
            stock_marca()
        if op=="2":
            menu_busqueda()
        if op=="3":
            menu_actualizar()
        if op=="4":
            print("Saliendo del progrma...")
            break

menu()
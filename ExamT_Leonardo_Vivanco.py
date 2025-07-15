productos = {"modelo": ['marca', 'pantalla', 'RAM', 'disco', 'GB de DD', 'procesador', 'video']}
stock = {"modelo": ["precio", "stock"]}
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
 '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
 'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
 'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
 'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
 '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
 '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
 'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
            }
stock = {'8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
 'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
 'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
        }       

def stock_marca():
    marca=input("Ingrese la marca que desea saber su stock: ")
    if marca not in productos:
        print(f"El stock es: {stock["modelo"][1]}")
    else:
        print("El stock es: 0")

def búsqueda_precio():
    while True:
        try:
            p_min=int(input("Ingrese precio mínimo: "))
            p_max=int(input("Ingrese precio máximo: "))
            if p_min<p_max:
                if stock["modelo"][0]>=p_min and stock["modelo"][0]<=p_max and stock["modelo"][1]>0:
                    print(f"Los notebooks entre los precios consultados son: [{productos["modelo"][0]},{productos["modelo"]}]")
                    return
                else:
                    print("No hay notebooks en ese rango de precios.")
                    return
        except:
            if p_min is not int:
                print("Debe ingresar valores enteros!!")
            elif p_max is not int:
                print("Debe ingresar valores enteros!!")

def actualizar_precio():
    while True:
        modelo=input("Ingrese modelo a actualizar: ")
        p=int(input("Ingrese precio nuevo: "))
        if modelo not in stock["modelo"]:
            print("El modelo no existe!!")
        else:
            stock["modelo"][1]=p
            print("Precio actualizado!!")

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
        elif op=="2":
            búsqueda_precio()
        elif op=="3":
            actualizar_precio()
        elif op=="4":
            print("Programa finalizado")
            break
        else:
            print("Debe seleccionar una opción valida!!")

menu()
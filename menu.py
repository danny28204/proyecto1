
productos = {}

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio unitario de {nombre}: "))
    productos[nombre] = {"precio": precio, "cantidad": 0}  

def ingresar_cantidad():
    print("\nProductos disponibles:")
    for producto in productos:
        print(f"{producto} - Precio: {productos[producto]['precio']}")
    
    nombre = input("\nIngrese el nombre del producto para el que desea ingresar la cantidad: ")
    
    if nombre in productos:
        cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
        productos[nombre]["cantidad"] = cantidad
    else:
        print("El producto no existe.")

def calcular_totales():
    total_general = 0
    print("\nTotales:")
    for producto, datos in productos.items():
        total_producto = datos["precio"] * datos["cantidad"]
        total_general += total_producto
        print(f"{producto} - Cantidad: {datos['cantidad']} - Total: ${total_producto:.2f}")
    
    print(f"\nTotal general: ${total_general:.2f}")

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Ingresar un producto")
        print("2. Ingresar cantidad de productos")
        print("3. Calcular totales")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_producto()
        elif opcion == "2":
            ingresar_cantidad()
        elif opcion == "3":
            calcular_totales()
        elif opcion == "4":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

mostrar_menu()

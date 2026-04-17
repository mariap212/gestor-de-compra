# Gestor de Compras

compras = []

def agregar_articulo():
    producto = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Precio inválido. Debe ser un número.")
        return
    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Cantidad inválida. Debe ser un número entero.")
        return
    articulo = {
        'producto': producto,
        'precio': precio,
        'cantidad': cantidad
    }
    compras.append(articulo)
    print("Artículo agregado exitosamente.")

def ver_lista():
    if not compras:
        print("La lista de compras está vacía.")
        return
    for articulo in compras:
        print(f"Producto: {articulo['producto']}, Precio: {articulo['precio']}, Cantidad: {articulo['cantidad']}")

def calcular_total():
    total = sum(articulo['precio'] * articulo['cantidad'] for articulo in compras)
    print(f"El total de la compra es: {total}")

def eliminar_articulo():
    producto = input("Ingrese el nombre del producto a eliminar: ")
    for articulo in compras:
        if articulo['producto'] == producto:
            compras.remove(articulo)
            print("Artículo eliminado exitosamente.")
            return
    print("Producto no encontrado.")

def main():
    while True:
        print("\n--- Gestor de Compras ---")
        print("1. Agregar artículo")
        print("2. Ver lista de compras")
        print("3. Calcular total")
        print("4. Eliminar artículo")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_articulo()
        elif opcion == '2':
            ver_lista()
        elif opcion == '3':
            calcular_total()
        elif opcion == '4':
            eliminar_articulo()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
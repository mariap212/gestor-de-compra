# Búsqueda en Lista

numeros = [12, 45, 78, 23, 56, 89, 34, 67]

def buscar_numero(numero):
    try:
        return numeros.index(numero)
    except ValueError:
        return -1


def numeros_mayores(umbral):
    return [n for n in numeros if n > umbral]


def promedio_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def ordenar_lista(lista):
    return sorted(lista)


def main():
    while True:
        print("\n--- Búsqueda en Lista ---")
        print("1. Buscar número")
        print("2. Números mayores que un umbral")
        print("3. Promedio de la lista")
        print("4. Ordenar lista")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = int(input("Ingrese el número a buscar: "))
            indice = buscar_numero(numero)
            if indice != -1:
                print(f"El número {numero} se encuentra en el índice {indice}.")
            else:
                print(f"El número {numero} no está en la lista.")
        elif opcion == '2':
            umbral = int(input("Ingrese el umbral: "))
            mayores = numeros_mayores(umbral)
            print(f"Números mayores que {umbral}: {mayores}")
        elif opcion == '3':
            promedio = promedio_lista(numeros)
            print(f"El promedio de la lista es: {promedio}")
        elif opcion == '4':
            ordenada = ordenar_lista(numeros)
            print(f"Lista ordenada: {ordenada}")
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == '__main__':
    main()
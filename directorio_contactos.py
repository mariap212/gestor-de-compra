# Directorio de Contactos

contactos = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el teléfono: ")
    ciudad = input("Ingrese la ciudad: ")
    contactos[nombre] = {
        'email': email,
        'telefono': telefono,
        'ciudad': ciudad
    }
    print("Contacto agregado exitosamente.")

def ver_contactos():
    if not contactos:
        print("El directorio está vacío.")
        return
    for nombre, datos in contactos.items():
        print(f"Nombre: {nombre}")
        print(f"  Email: {datos['email']}")
        print(f"  Teléfono: {datos['telefono']}")
        print(f"  Ciudad: {datos['ciudad']}")
        print()

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    contacto = contactos.get(nombre)
    if contacto:
        print(f"Nombre: {nombre}")
        print(f"Email: {contacto['email']}")
        print(f"Teléfono: {contacto['telefono']}")
        print(f"Ciudad: {contacto['ciudad']}")
    else:
        print("Contacto no encontrado.")

def actualizar_telefono():
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in contactos:
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")
        contactos[nombre]['telefono'] = nuevo_telefono
        print("Teléfono actualizado exitosamente.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if contactos.pop(nombre, None):
        print("Contacto eliminado exitosamente.")
    else:
        print("Contacto no encontrado.")

def main():
    while True:
        print("\n--- Directorio de Contactos ---")
        print("1. Agregar contacto")
        print("2. Ver todos los contactos")
        print("3. Buscar por nombre")
        print("4. Actualizar teléfono")
        print("5. Eliminar contacto")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            actualizar_telefono()
        elif opcion == '5':
            eliminar_contacto()
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

import random
import string

def generar_contraseña(longitud, mayusculas, minusculas, alfanumericos, simbolos):
    
    caracteres_disponibles = ""
    
    if mayusculas:
        caracteres_disponibles += string.ascii_uppercase  # Mayúsculas
    if minusculas:
        caracteres_disponibles += string.ascii_lowercase  # Minúsculas
    if alfanumericos:
        caracteres_disponibles += string.digits  # Dígitos
    if simbolos:
        caracteres_disponibles += string.punctuation  # Símbolos

    
    if not caracteres_disponibles:
        print("Error: Debes seleccionar al menos una categoría de caracteres.")
        return None

    contraseña = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    return contraseña

def mostrar_menu():
    print("\nGenerador de Contraseñas Seguras")
    print("1. Longitud de la contraseña")
    print("2. Incluir mayúsculas")
    print("3. Incluir minúsculas")
    print("4. Incluir caracteres alfanuméricos")
    print("5. Incluir símbolos")
    print("6. Generar contraseña")
    print("7. Salir")

def main():
    print("¡Bienvenido al Generador de Contraseñas Seguras!")
    print("Este programa te permite generar contraseñas seguras personalizadas.")
    
    longitud = 8
    mayusculas = False
    minusculas = False
    alfanumericos = False
    simbolos = False

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 4): "))
            if longitud < 4:
                print("La longitud debe ser al menos 4 caracteres.")
                longitud = 8  

        elif opcion == "2":
            mayusculas = not mayusculas
            print(f"Incluir mayúsculas: {'Sí' if mayusculas else 'No'}")

        elif opcion == "3":
            minusculas = not minusculas
            print(f"Incluir minúsculas: {'Sí' if minusculas else 'No'}")

        elif opcion == "4":
            alfanumericos = not alfanumericos
            print(f"Incluir caracteres alfanuméricos: {'Sí' if alfanumericos else 'No'}")

        elif opcion == "5":
            simbolos = not simbolos
            print(f"Incluir símbolos: {'Sí' if simbolos else 'No'}")

        elif opcion == "6":
            contraseña = generar_contraseña(longitud, mayusculas, minusculas, alfanumericos, simbolos)
            if contraseña:
                print(f"Contraseña generada: {contraseña}")

        
            otra = input("¿Quieres generar otra contraseña? (s/n): ").lower()
            if otra != "s":
                print("¡Gracias por usar el Generador de Contraseñas Seguras!")
                break

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor selecciona una opción entre 1 y 7.")

if __name__ == "__main__":
    main()



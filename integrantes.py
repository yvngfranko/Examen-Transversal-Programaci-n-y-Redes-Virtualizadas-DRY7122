def mostrar_integrantes():
    integrantes = [
        {"nombre": "Ian", "apellido": "Munoz"},
        {"nombre": "Diego", "apellido": "Gonzalez"},
        {"nombre": "Franco", "apellido": "Valdebenito"}
    ]
    
    print("\nLista de integrantes del grupo:")
    print("-----------------------------")
    for i, integrante in enumerate(integrantes, 1):
        print(f"{i}. {integrante['nombre']} {integrante['apellido']}")
    print()

if __name__ == "__main__":
    mostrar_integrantes()

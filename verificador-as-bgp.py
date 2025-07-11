def verificar_as():
    print("\nVerificador de AS BGP :)")
    print("--------------------")

    try:
        as_number = int(input("Ingrese el número de AS: "))

        private_as_ranges = [
            (64512, 65534),
            (4200000000, 4294967294)
        ]

        if as_number == 0 or as_number == 65535 or as_number == 4294967295:
            print(f"El AS {as_number} está reservado y no debe usarse.")
        elif any(start <= as_number <= end for start, end in private_as_ranges):
            print(f"El AS {as_number} es un AS privado.")
        elif (1 <= as_number <= 64495) or (65536 <= as_number <= 4199999999):
            print(f"El AS {as_number} es un AS público.")
        else:
            print(f"El AS {as_number} no está en un rango válido.")

    except ValueError:
        print("Error: Por favor ingrese un número válido.")
    print()

if __name__ == "__main__":
    verificar_as()

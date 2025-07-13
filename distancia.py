import requests
import json
import time


while True:
    print('###############################')
    print('BIENVENIDO AL BUSCADOR DE RUTAS')
    print('###############################')
    print('1. Para comenzar el menu')
    print('s. Para salir del menu')
    opc = input('Ingrese una opcion valida: ')

    if opc == '1':
        key = "99485d02-70c2-4809-8c3b-7e41fa57cb95"
        ciudad1 = input('Ingrese el nombre de su primera ciudad: ')
        ciudad2 = input('Ingrese el nombre de su segunda ciudad: ')
        
        profile = input('Ingrese el medio de transporte (foot, bike, ecargobike, car, small_truck, truck, scooter): ')

        base1 = f"https://graphhopper.com/api/1/geocode?q={ciudad1}&locale=de&key={key}"
        req1 = requests.get(base1).json()
        base2 = f"https://graphhopper.com/api/1/geocode?q={ciudad2}&locale=de&key={key}"
        req2 = requests.get(base2).json()

        lat1 = req1['hits'][0]['point']['lat']
        lon1 = req1['hits'][0]['point']['lng']
        cord1 = f'{lat1},{lon1}'

        lat2 = req2['hits'][0]['point']['lat']
        lon2 = req2['hits'][0]['point']['lng']
        cord2 = f'{lat2},{lon2}'

        url = f'https://graphhopper.com/api/1/route?point={cord1}&point={cord2}&profile={profile}&locale=de&calc_points=false&key={key}'
        resultado = requests.get(url).json()

        distancia = resultado['paths'][0]['distance']
        millas = distancia / 1609
        kilometros = distancia / 1000

        tiempo = resultado['paths'][0]['time']
        horas = tiempo /  3600000

        print('')
        print(f'El viaje en millas son: {millas} millas')
        print(f'El viaje en kilometros son: {kilometros} km')
        print(f'El viaje durara aproximadamente: {horas} hrs')
    
    elif opc == '2':
        break

    else:
        print('Opcion ingresada incorrecta, vuelva a intentarlo')

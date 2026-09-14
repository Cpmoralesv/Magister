"""
lista=[

    ['Santiago', 'Puerto Montt', 35000, 30, '11-01-2024'],

    ['Santiago', 'Concepción', 30000, 40, '12-02-2024'],

    ['Concepción', 'Puerto Montt', 22000, 50, '13-02-2024'],

    ['Santiago', 'Puerto Montt', 20000, 2, '19-01-2024'],

    ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024'],

    ['Concepción', 'Puerto Montt', 22000, 50, '25-01-2024'],

    ['Antofagasta', 'Santiago', 27000, 14, '08-04-2024']

]
def vuelos_disponibles(vuelos, origen, destino, pasajeros):
            viajes_disponibles=[]
            for viaje in lista:
                origen_lista = viaje[0]
                destino_lista = viaje[1]
                asientos_disponibles = viaje[3]
                if (origen_lista.lower() == origen.lower()
                    and destino_lista.lower() == destino.lower()
                    and asientos_disponibles >= pasajeros):
                    viajes_disponibles.append(viaje)
            return viajes_disponibles

resultado= vuelos_disponibles(lista,"Santiago","Puerto Montt",2)
print(resultado)


lista=[

    ['Santiago', 'Puerto Montt', 35000, 30, '11-01-2024'],

    ['Santiago', 'Concepción', 30000, 40, '12-02-2024'],

    ['Concepción', 'Puerto Montt', 22000, 50, '13-02-2024'],

    ['Santiago', 'Puerto Montt', 20000, 2, '19-01-2024'],

    ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024'],

    ['Concepción', 'Puerto Montt', 22000, 50, '25-01-2024'],

    ['Antofagasta', 'Santiago', 27000, 14, '08-04-2024']

]

def vuelo_mas_barato(vuelos, origen, destino):
    viajes_disponibles = []
    for viaje in lista:
        origen_lista = viaje[0]
        destino_lista = viaje[1]
        pecio_lista = viaje[2]
        if (origen_lista.lower() == origen.lower()
                and destino_lista.lower() == destino.lower()):
            viajes_disponibles.append(viaje)
        if not viajes_disponibles:
            return None
        barato_disponibles = min(viajes_disponibles, key=lambda x:x[2])

    return barato_disponibles

resultado= vuelo_mas_barato(lista,"Santiago","Puerto Montt")
print(resultado)


"""
vuelos=[

    ['Santiago', 'Puerto Montt', 35000, 30, '11-01-2024'],

    ['Santiago', 'Concepción', 30000, 40, '12-02-2024'],

    ['Concepción', 'Puerto Montt', 22000, 50, '13-02-2024'],

    ['Santiago', 'Puerto Montt', 20000, 2, '19-01-2024'],

    ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024'],

    ['Concepción', 'Puerto Montt', 22000, 50, '25-01-2024'],

    ['Antofagasta', 'Santiago', 27000, 14, '08-04-2024']

]
def aplicar_descuento(vuelos, origen, destino, porcentaje):
    viajes_modificados = []
    for viaje in vuelos:
        origen_lista = viaje[0]
        destino_lista = viaje[1]
        precio_descuento = int(viaje[2]*porcentaje)
        if (origen_lista.lower() == origen.lower()
                and destino_lista.lower() == destino.lower()):
            viaje[2] = int(precio_descuento)
        viajes_modificados.append(viaje)

    return viajes_modificados

resultado=aplicar_descuento(vuelos,"Santiago","Puerto Montt",0.5)
print(resultado)
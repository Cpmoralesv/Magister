vuelos=[

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
    for viaje in vuelos:
        origen_lista = viaje[0]
        destino_lista = viaje[1]
        pecio_lista = viaje[2]
        if (origen_lista.lower() == origen.lower()
                and destino_lista.lower() == destino.lower()):
            viajes_disponibles.append(viaje)

    if not viajes_disponibles:
        return []
    vuelo_barato=viajes_disponibles[0]

    for viaje in viajes_disponibles:
            precio_actual = viaje[2]
            precio_campeon_actual = vuelo_barato[2]

            # Si encontramos uno más barato, lo coronamos como el nuevo campeón
            if precio_actual < precio_campeon_actual:
                vuelo_barato = viaje

    return vuelo_barato


resultado= vuelo_mas_barato(vuelos,"Concepción","Puerto Montt")
print(resultado)
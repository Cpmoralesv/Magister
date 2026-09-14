from Prueba import resultado

vuelos=[


   ['Santiago', 'Puerto Montt', 35000, 30, '11-01-2024'],


   ['Santiago', 'Concepción', 30000, 40, '12-02-2024'],


   ['Concepción', 'Puerto Montt', 22000, 50, '13-02-2024'],


   ['Santiago', 'Puerto Montt', 20000, 2, '19-01-2024'],


   ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024'],


   ['Concepción', 'Puerto Montt', 22000, 50, '25-01-2024'],


   ['Antofagasta', 'Santiago', 27000, 14, '08-04-2024']


]


def vuelos_con_escala(vuelos, origen, destino):
    escalas = []

    for vuelo1 in vuelos:
        origen_1 = vuelo1[0]
        destino_1 = vuelo1[1]
        fecha_1 = vuelo1[4]

        if origen_1.lower() == origen.lower():
            for vuelo2 in vuelos:
                origen_2 = vuelo2[0]
                destino_2 = vuelo2[1]
                fecha_2 = vuelo2[4]

                if (destino_1.lower() == origen_2.lower()
                        and destino_2.lower() == destino.lower()):

                    if fecha_1 < fecha_2:
                        par_de_vuelos = (vuelo1, vuelo2)
                        escalas.append(par_de_vuelos)

    return escalas

resultado =vuelos_con_escala(vuelos,'Santiago','Puerto Montt')
print(resultado)
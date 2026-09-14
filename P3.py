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
def aplicar_descuento(vuelos, origen, destino, porcentaje):
   viajes_modificados = []

   for viaje in vuelos:
       origen_lista = viaje[0]
       destino_lista = viaje[1]

       if (origen_lista.lower() == origen.lower()
               and destino_lista.lower() == destino.lower()):
            precio_descuento = int(viaje[2] * (1 - porcentaje))
            viaje[2] = precio_descuento
   return vuelos

resultado=aplicar_descuento(vuelos,'Santiago','Puerto Montt',0.2)
print(resultado)
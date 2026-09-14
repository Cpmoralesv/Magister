"""
class Mascota:
# Constructor y atributos
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

# Método (acción)
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy un {self.especie}"


# Creando un objeto de tipo "Mascota"
mi_perro = Mascota("Rex", "Perro")
print(mi_perro.saludar())

mi_bolsa = (99, 10)
print(mi_bolsa)


a=99
b=10

a,b=a,b


lista = ['Alicia', 1998, 'Bob', 1990, 'Carlos', 1986, 'David', 2001]
print(lista)

for i in range(len(lista)//2):

    nombre = lista[2*i]

    nacimiento = lista[2*i+1]

    print(nombre, nacimiento)

lista = ['soleado', 'nublado', 'soleado', 'lluvia', 2.4, 'lluvia', 0.1, 'nublado', 'lluvia', 0.8]

print(lista)

suma = 0

for elemento in lista:

    if elemento not in ['soleado','nublado', 'lluvia']:

        suma += elemento

print(suma)


d = ['Alicia', 'Bob', 'Carlos', 'David']

m = ['Pelusa', 'Luke', 'Mickey', 'Madonna']


for i in range(len(d)):

    print(d[i], m[i])


lista = ['Alicia', 'Bob', 'Carlos', 'David']

while len(lista) > 0:

    ultimo_cliente = len(lista)-1

    cliente = lista.pop(ultimo_cliente)

    print(cliente)

lista = [1, 2, 4, 5, 6, 7, 8, 9]

lista.insert(2, 3)
print(lista)
print(len(lista))

seguidores_por_dia = [120, 150, 90]

for cantidad in seguidores_por_dia:
    print(cantidad)


tupla = ('Camila', 5.0, 6.2, 4.8, 6.0)


def calcular_promedio(tupla):
        nombre = tupla[0]
        notas = tupla[1:]
        promedio= sum(notas)/(len(notas))
        return (nombre,promedio)

print(calcular_promedio(tupla))


lista = [-40, -1, 2, 5, 16, 72, 100]
print(lista)


def agregar_entero(lista, entero):
        for i in range(len(lista)):
            if entero<lista[i]:
                lista.insert(i,entero)
                return lista

        lista.append(entero)
        return lista

resultado= agregar_entero(lista, -13)
print(resultado)



lista = [1, 4, 3, 1, 4, 2, 5, 1, 2, 4, 1, 3, 1, 2, 4]


def contar_repeticiones(lista):
    if not lista:
        return 0
    max_repeticiones=0
    for elemento in lista:
        frecuencia=lista.count(elemento)
        if frecuencia>max_repeticiones:
            max_repeticiones=frecuencia
    return max_repeticiones



lista = ['Francisca Avedaño', 'Pablo Avedaño', 'Juan Bravo', 'Javiera Hernández', 'Mario Huerta', 'David Morales', 'Eliza Morales']

def agregar_estudiante(lista, estudiante):
    estudiante_apellido=estudiante.split()[-1]
    for i in range(len(lista)):
      actual_apellido = lista[i].split()[-1]
      if (estudiante_apellido,estudiante) < (actual_apellido,lista[i]):
          lista.insert(i,estudiante)
          return lista

    lista.append(estudiante)
    return lista


lista = [-40, -1, 2, 5, 16, 72, 100]
print(lista)


def comentarios_instagram(lista, entero):
        for i in range(len(lista)):
            if entero<lista[i]:
                lista.insert(i,entero)
                return lista

        lista.append(entero)
        return lista

resultado= comentarios_instagram(lista, 1000000)
print(resultado)


lista = [1, 20, 2, 40, 3, 6, 100]
print(lista)
def dia_mas_lluvioso(lista)
    resultado=[]
    return resultado


lluvias = ['Enero',1,10,2,50,10,2,12,80,14,8,20,100,

           'Febrero',4,10,5,12,6,200,

           'Abril',1,45,

           'Julio',12, 34, 14, 13, 20, 90, 21, 32,

           'Noviembre',3,45,8,120,20,10]

print(lluvias)




L = [  [ 3,2,1  ],   [ 4,5,6] ]
print(L)

largo=len(L)
print(largo)

votos = [

    ['Alicia', 50],

    ['Bob', 42],

    ['Carlos', 29],

    ['David', 100]

]

mejor = ['', 0]

for candidato in votos:

    if candidato[1] > mejor[1]:

        mejor = candidato

print(mejor[0])


lista = [

    [-1, 2, -5, 40],

    [9, 65, -6, -34],

    [0, -4, 9, 2]

]

print(lista)


fils = len(lista)

cols = len(lista[0])

for i in range(fils):

    for j in range(cols):

        if lista[i][j] < 0:

            lista[i][j] = 0

print(lista)



lista = [

    ['', 'YYZZ', 'ZY', ''],

    ['YZZY', 'YY', 'Y', 'YZYY'],

    ['Y', 'YZ', 'YZ', 'Y']

]

cuenta = 0

for fila in lista:

    for dato in fila:

        cuenta += dato.count('Y')

print(cuenta)



 if ingredites_amigos_todos != ingredientes_favoritos:
            ingredientes_compras.append(ingredientes_amigos[i])
            print(ingredientes_compras)





lo_que_trajeron= []
for cajita_amigo in ingredientes_amigos:
    for ingrediente in cajita_amigo:
        lo_que_trajeron.append(ingrediente)


lista_final_compras= []
for favorito in ingredientes_favoritos:
    if favorito not in lo_que_trajeron:
        lista_final_compras.append(favorito)

print(lista_final_compras)

ingredientes_amigos = [

    ['Pan', 'Salchichas', 'Mostaza', 'Ketchup'],

    ['Pan', 'Tomate', 'Chucrut'],

    ['Ketchup', 'Salchichas'],

    ['Chucrut', 'Pan']

]

ingredientes_favoritos = ['Pan', 'Tomate', 'Salchichas', 'Chucrut', 'Mostaza', 'Ketchup', 'Mayonesa', 'Palta']

for amigo in ingredientes_amigos:

    for ingrediente in amigo:

        if ingrediente in ingredientes_favoritos:

            ingredientes_favoritos.remove(ingrediente)

print(ingredientes_favoritos)





lista = [

    [0, 1, 2, 3, 4],

    [0, 1, 2, 3, 4],

    [0, 1, 2, 3, 4],

    [0, 1, 2, 3, 4],

    [4, 0, 2, 3, 1],

    [4, 0, 2, 3, 1],

    [0, 1, 2, 3, 4]

]


for lista_int in lista:
    if lista.count(lista_int) == 1:
        print(lista_int)




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
                if (origen.lower() == origen.lower()
                    and destino.lower() == destino.lower()
                    and asientos_disponibles >= pasajeros):
                    viajes_disponibles.append(viaje)
            return viajes_disponibles

resultado= vuelos_disponibles(lista,"Santiago","Puerto Montt",2)
print(resultado)


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
    for viaje in lista:
        origen_lista = viaje[0]
        destino_lista = viaje[1]
        pecio_lista = viaje[2]
        if (origen_lista.lower() == origen.lower()
                and destino_lista.lower() == destino.lower()):
            viajes_disponibles.append(viaje)
    return viajes_disponibles

resultado= vuelo_mas_barato(lista,"Santiago","Puerto Montt")
print(resultado)



from collections import deque
cola = deque()
def agregar_auto(cola, descripción, tiempo):
    auto = (descripción, tiempo)
    cola.append(auto)
    print("Acaba de llegar", descripción, "a la cola")

def arreglar_auto (cola):
    auto = cola.popleft()
    print("Arreglamos el auto", auto [0], "nos tardamos", auto[1])

while True:
    eleccion = input("(1) agregar auto (2) arreglar auto:")
    if eleccion == "1":
        descripcion = input()
        tiempo =  int(input())
        agregar_auto (cola, descripcion, tiempo)

    elif eleccion == "2":
        if cola:  # Verificamos que haya autos en la cola
            arreglar_auto(cola)
        else:
            print("No hay autos para arreglar.")


from collections import deque

deq = deque((1, 4, 5, 3, 2))



print(deq.count(1))

print(deq.pop())

print(deq.pop())

print(deq.popleft())

print(deq.popleft())



from collections import deque

deq = deque(('You', 'Community','Breaking Bad'))
print(deq)

series = deque()

series.append('You')

series.append('Community')

series.append('Breaking Bad')

series.popleft()
print(series)

from collections import deque
fila1 = deque(('p1', 'p2'))
fila2 = deque(('p1',))


fila3 = deque(('p1', 'p2','p3'))

filas = (fila1, fila2, fila3)

from collections import deque

# Setup correcto de las filas
fila1 = deque(['p1', 'p2'])
fila2 = deque(['p1'])
fila3 = deque(['p1', 'p2', 'p3'])
filas = (fila1, fila2, fila3)


def elegir_fila(filas, cliente):
    # 1. Asumimos que la primera es la mejor inicialmente
    mejor_fila = filas[0]

    # 2. Buscamos si hay alguna más corta
    for fila in filas:
        if len(fila) < len(mejor_fila):
            mejor_fila = fila

    # 3. Agregamos al cliente al FINAL de la fila (respetando FIFO)
    mejor_fila.append(cliente)

    print(f"El cliente {cliente} fue agregado. Así quedó la fila elegida: {mejor_fila}")


# Probamos la función
elegir_fila(filas, 'p_nuevo')



historial = [
    ["escribir", "Hola mundo", 1],
    ["cambiar_color", "Rojo", 1],
    ["borrar", "Texto extra", 2]
]

def deshacer_acciones(pila_acciones):

    while historial:
        ultima_accion = historial.pop()
        accion = ultima_accion[0]
        que_accion = ultima_accion[1]
        fila = ultima_accion[2]

        print("Se esta deshaciendo:", accion, "especificamente:", que_accion, "en numero de linea:", fila)

deshacer_acciones(historial)
print(historial)



def editor_interactivo(pila_historial):
    # Creamos una segunda pila vacía para guardar lo que vamos deshaciendo
    pila_rehacer = []

    while True:
        # Mostramos cuántas acciones hay en cada pila para guiarnos
        print("\n--- ESTADO DEL EDITOR ---")
        print(f"Acciones para deshacer: {len(pila_historial)}")
        print(f"Acciones para rehacer: {len(pila_rehacer)}")

        # Le pedimos al usuario que elija una acción
        comando = input("Escribe un comando (deshacer / rehacer / salir): ").lower()

        if comando == "deshacer":
            if len(pila_historial) > 0:
                # 1. Sacamos la última acción del historial
                accion_deshecha = pila_historial.pop()

                # 2. La guardamos en la pila de rehacer por si nos arrepentimos
                pila_rehacer.append(accion_deshecha)

                print(f"-> DESHICIMOS: {accion_deshecha[0]} ('{accion_deshecha[1]}')")
            else:
                print("-> No hay nada más que deshacer.")

        elif comando == "rehacer":
            if len(pila_rehacer) > 0:
                # 1. Sacamos la última acción que habíamos deshecho
                accion_rehecha = pila_rehacer.pop()

                # 2. La devolvemos al historial principal
                pila_historial.append(accion_rehecha)

                print(f"-> REHICIMOS: {accion_rehecha[0]} ('{accion_rehecha[1]}')")
            else:
                print("-> No hay nada para rehacer.")

        elif comando == "salir":
            print("Saliendo del editor...")
            break  # Rompemos el ciclo infinito

        else:
            print("Comando no reconocido. Intenta de nuevo.")


# Nuestra lista de prueba inicial
historial = [
    ["escribir", "Hola mundo", 1],
    ["cambiar_color", "Rojo", 1],
    ["borrar", "Texto extra", 2]
]

# Ejecutamos la función
editor_interactivo(historial)


from collections import deque


def atender_soporte(cola_tickets):

        while tickets:
            primero_fila = tickets.popleft()
            cliente = primero_fila[0]
            problema = primero_fila[1]
            print("Se esta atendiendo:", cliente, "el problema:", problema)


tickets = deque([
    ["María Silva", "internet", 2],
    ["Carlos Rojas", "password", 1],
    ["Lucía Pérez", "impresora", 3]
])

atender_soporte(tickets)
print(tickets)

from collections import deque


def atender_soporte(cola_tickets):
    # Usamos el parámetro de la función y convertimos a deque si es una lista normal
    cola = deque(cola_tickets)

    while cola:
        # Extraemos al primero de la fila de manera eficiente
        primero_fila = cola.popleft()
        cliente = primero_fila[0]
        problema = primero_fila[1]

        # El print va indentado AQUÍ ADENTRO para que se imprima por cada ticket
        print("Se esta atendiendo:", cliente, "el problema:", problema)


# Lista de prueba
tickets = [
    ["María Silva", "internet", 2],
    ["Carlos Rojas", "password", 1],
    ["Lucía Pérez", "impresora", 3]
]

atender_soporte(tickets)


from collections import deque
def lavar_pila(pila, instrucciones):
    for instruccion in instrucciones:
        if instruccion[0] == 'lavar':
            pila.pop()
        elif instruccion[0] == 'nuevo':
            utensilio = (instruccion[1])
            pila.append(utensilio)
    return pila

pila = deque(['plato', 'sartén', 'bowl'])
instrucciones = [('lavar',), ('lavar',), ('nuevo', 'cuchara'), ('lavar',)]
resultado = lavar_pila(pila, instrucciones)
print(resultado)






from collections import deque
cola = deque(['María', 'Felipe', 'Carlos'])
instrucciones = [('nueva', 'Alejandra'), ('atender',), ('colar', 'Rocío', 1), ('atender',)]

def atender_cola(cola, instrucciones):
    for instruccion in instrucciones:
        if instruccion[0] == 'atender':
            cola.popleft()
        elif instruccion[0] == 'nueva':
            agregar = (instruccion[1])
            cola.append(agregar)
        elif instruccion[0] == 'colar':
            agregar = instruccion[1]
            posicion = instruccion[2]
            cola.insert(posicion,agregar)
    return cola



from collections import deque
def intercalar_colas(cola_1, cola_2):
    cola_3 = deque()

    while cola_1 or cola_2:
        if cola_1:
            primer_ingreso = cola_1.popleft()
            cola_3.append(primer_ingreso)
        if cola_2:
            segundo_ingreso = cola_2.popleft()
            cola_3.append(segundo_ingreso)

    return cola_3

resultado = intercalar_colas(cola_1, cola_2)
print(resultado)

from collections import deque
cola = deque([4, -1, -3, 6, -100, 5])
from collections import deque
def ordenar_cola(cola):
    lista_temp = list(cola)
    lista_temp.sort()
    cola_ordenada = deque(lista_temp)
    return cola_ordenada

resultado = ordenar_cola(cola)
print(resultado)


proyectos =    [
    ["MUSEO", "BLABLA"],
["GAME", "BLABLA"]
["PM", "BLABLA"]
]

def preguntas_proyectos(nombre,descripcion):
    if nombre in proyectos:
        nombre = proyectos[0]
        descripcion = proyectos[1]

###DICCIONARIO
# Preguntar cuantos proyectos son
cantidad = int(input("Cuantos proyectos son? "))

# Anotar los proyectos
proyectos = {}
for i in range(cantidad):
    nombre = input("Nombre del proyecto? ")
    descripcion = input("Descripcion del proyecto? ")
    proyectos[nombre] = descripcion  # Aquí guardamos la llave y su valor

# Mostrar los proyectos
print("Estos son los proyectos:")
for nombre, descripcion in proyectos.items():
    print(f"{nombre} => {descripcion}")


postulantes_museo = set(['Victor', 'Fernanda', 'Veronica'])
postulantes_game = set(['Victor', 'Luciano', 'Rene', 'Valeria'])
postulantes_pm = set(['Victor', 'Fernanda'])


postulantes_unicos = postulantes_museo | postulantes_game | postulantes_pm

cantidad_postulantes=len(postulantes_unicos)

print(cantidad_postulantes)


poema = ['Mis', 'pasos', 'en', 'esta', 'calle', 'Resuenan', 'En', 'otra', 'calle', 'Donde', 'Oigo', 'mis', 'pasos', 'Pasar', 'en', 'esta', 'calle', 'Donde', 'Sólo', 'es', 'real', 'la', 'niebla']



prohibidas = set(['calle', 'mis', 'pasos'])

for eliminar in poema
    if eliminar=prohibdas
    eliminar_final
    poema=pop.eliminar_final


lista = [1,2,1,1,5,6,4,4,4,6,7,5,1,1,7,7,7,2,1,2]


d = dict()

for num in set(lista):

    d[num] = lista.count(num)

print(d)

clientes = {

    'Alicia': (28, 'Chile', 1200),

    'Bob': (45, 'Francia', 2000),

    'Carlos': (30, 'Argentina', 500),

    'David': (23, 'Inglaterra', 0)

}

for cliente in clientes:

    edad, residencia, deuda = clientes[cliente]

    if deuda > 1000:

        print(cliente)


amigos = {

            'Bob': ['Patricio', 'Calamardo', 'Arenita', 'Don Cangrejo'],

            'Patricio': ['Bob', 'Calamardo'],

            'Arenita': ['Bob'],

            'Calamardo': [],

            'Don Cangrejo': ['Bob', 'Calamardo']

        }
cuenta = dict()

for nombre in amigos:

    cuenta[nombre] = 0

for lista_amigos in amigos.values():

    for nombre in lista_amigos:

        cuenta[nombre] += 1

print(cuenta)



preferencias = {
    "Cata": ["Los Bunkers", "Coldplay", "Arctic Monkeys"],
    "Pedro": ["Coldplay", "Dua Lipa", "Rosalia"],
    "Juan": ["Los Bunkers", "Rosalia", "Arctic Monkeys", "Metallica"],
    "Sofi": ["Dua Lipa", "Coldplay", "Metallica"]
}

preferencias = {
    "Cata": ["Los Bunkers", "Coldplay", "Arctic Monkeys"],
    "Pedro": ["Coldplay", "Dua Lipa", "Rosalia"],
    "Juan": ["Los Bunkers", "Rosalia", "Arctic Monkeys", "Metallica"],
    "Sofi": ["Dua Lipa", "Coldplay", "Metallica"]
}


def bandas_unicas(diccionario):
    conteo = {}

    # Recorremos los valores (las listas de bandas de cada persona)
    for lista_bandas in diccionario.values():
        for banda in lista_bandas:
            # Contamos cuántas veces aparece cada banda
            conteo[banda] = conteo.get(banda, 0) + 1

    # Usamos .keys() para obtener solo las bandas únicas sin repetir
    return list(conteo.keys())



resultado=bandas_unicas(preferencias)
print(resultado)





def precio_total(boletas):
    total = 0
    for boleta in boletas:
        total += int(boleta['precio'])
    return total


suma=precio_total(boletas)
print(suma)







def precio_por_mes(boletas):
    desglose = dict()
    for boleta in boletas:
        fecha = boleta['fecha_compra']
        periodo = fecha[3:]

        precio = int(boleta['precio'])
        if periodo in desglose:
            desglose[periodo] += precio
        else:
            desglose[periodo] = precio

    return desglose


nuevo_diccionario=precio_por_mes(boletas)
print(nuevo_diccionario)


def productos_frecuentes(boletas):
    if not boletas:
        return set()

    total_boletas = len(boletas)
    conteo_productos = {}

    for boleta in boletas:

        for producto in boleta['productos'].keys():
            conteo_productos[producto] = conteo_productos.get(producto, 0) + 1

    resultado = set()
    for producto, frecuencia in conteo_productos.items():
        if frecuencia >= total_boletas * 0.5:
            resultado.add(producto)

    return resultado

nuevo_diccionario=productos_frecuentes(boletas)
print(nuevo_diccionario)


boletas=[
    {
        'fecha_compra': '29-05-23',
        'precio': 11800,
        'productos': {
            'Chocolate': (1, 2300),
            'Mantequilla': (1, 2500),
            'Huevos': (12, 4000),
            'Pan': (1, 3000)
        }
    },
    {
        'fecha_compra': '31-05-23',
        'precio': 5200,
        'productos': {
            'Pan': (1, 3000),
            'Leche': (2, 2200)
        }
    },
    {
        'fecha_compra': '01-06-23',
        'precio': 6800,
        'productos': {
            'Mantequilla': (2, 5000),
            'Azúcar': (1, 1800)
        }
    }
]


def gasto_productos(boletas):
    gasto_total = dict()
    for boleta in boletas:
        for nombre_producto, datos in boleta['productos'].items():
            gasto = int(datos[1])
            if nombre_producto in gasto_total:
                gasto_total[nombre_producto] += gasto
            else:
                gasto_total[nombre_producto] = gasto
    return gasto_total


resultado=gasto_productos(boletas)
print(resultado)



class Planta:
    def __init__(self,especie:str,altura:int):
        self.especie=especie
        self.altura=altura


a = Planta( 'Washingtonia filifera', 15 )
print(a.especie)
print(a.altura)


class Casa:
    def __init__(self,direccion:str,piezas:int,banos:int,metros_cuadrados:float, urbana:bool):
        self.direccion=direccion
        self.piezas=piezas
        self.banos=banos
        self.metros_cuadrados=metros_cuadrados
        self.urbana=urbana

    def precio(self):
        if self.urbana == True:
            return (self.piezas+self.banos)*self.metros_cuadrados+100
        else:
            return (self.piezas+self.banos)*self.metros_cuadrados







c1 = Casa('Frente al mall 321', 1, 1, 20.0, True)
c2 = Casa('Frente al lago 123', 2, 2, 50.0, False)

print(c1.precio())
print(c2.precio())


class Menu:
    def __init__(self,comidas:str,precios:int):
        self.comidas=comidas
        self.precios=precios


    def __str__(self):

comidas = ['Pato a la mostaza', 'Hamburguesa', 'Ensalada', 'Lasagna']
precios = [20000, 8000, 6000, 9000]
menu = Menu(comidas, precios)

print(menu)
"""

class Enemigo:
    def __init__(self,nombre:str,vida:float,fuerza_de_ataque:float):
        self.nombre=nombre
        self.vida=vida
        self.fuerza_de_ataque=fuerza_de_ataque

    def recibir_ataque(self,dano):
        self.vida=self.vida-dano
        if self.vida < 0:
            self.vida=0

    def atacar(self,otro):
        otro.recibir_ataque(self.fuerza_de_ataque)

    def __str__(self):
        return f"{self.nombre} - {self.vida}"

a = Enemigo( 'Esqueleto', 8, 6 )
b = Enemigo( 'Zombie', 10, 5 )
print(a)
print(b)

a.recibir_ataque(5)
print(a)

a.atacar(b)
print(b)

a.atacar(b)
print(b)

# Universidad del Valle de Guatemala
# Base de Datos
# Marcos Gutierrez 
# 17909

import random
import sqlite3
conn = sqlite3.connect('parcial02.db')
# cursor de la basea de datos
c = conn.cursor()
'''
	cliente (id, nit, nombre, credito)
	tienda (id, nombre, direccion)
	compra (id, cliente_id, tienda_id, total, fecha)
'''

# creamos la tabla cliente
c.execute(
	'CREATE TABLE cliente(id INT PRIMARY KEY, nit INT, nombre VARCHAR(30) NOT NULL, credito FLOAT)'
)
# creamos la tabla de tienda
c.execute(
	'CREATE TABLE tienda(id INT PRIMARY KEY, nombre VARCHAR(30) NOT NULL, direccion VARCHAR(30) NOT NULL)'
)
# creamos la tabla de compras
c.execute(
	'''CREATE TABLE compra(
			id INT PRIMARY KEY, 
			cliente_id INT, 
			tienda_id INT,
			total FLOAT,
			fecha VARCHAR(30) NOT NULL,
			FOREIGN KEY (cliente_id) REFERENCES cliente (id),
			FOREIGN KEY (tienda_id) REFERENCES tienda (id)
		)			
	'''
)

# lista para ejecutar
nameList = [
    'Thelma',  
    'Yuriko'  ,
    'Mathew'  ,
    'Lavona'  ,
    'Jamal'  ,
    'Rochell' , 
    'Willia' , 
    'Glen'  ,
    'Jenelle' , 
    'Nelson' , 
    'Katelyn', 
    'Mackenzie' , 
    'Carman' , 
    'Lindsy' , 
    'Sheree' , 
    'Dorinda' , 
    'Jenae' , 
    'Janee' , 
    'Twana' , 
    'Yee' , 
    'Frederic' , 
    'Jaqueline' , 
    'Shelby' , 
    'Trista' , 
    'Daron' , 
    'Nikita' , 
    'Cristi',  
    'Margrett' , 
    'Chanel  '
]
# lista de apellidos
lastname = [
    ' Wilkins',
    ' Santana',
    ' Henderson',
    ' Sosa',
    ' Price',
    ' Church',
    ' Branch',
    ' Spencer',
    ' Sampson',
    ' Burton',
    ' Baker',
    ' Lin',
    ' Sheppard',
    ' Bray',
    ' Haney',
    ' Morales',
    ' Gilbert',
    ' Rosario',
    ' Rocha',
    ' Copeland'
]
# lista de avenidas
avenida = [
	'1ra Avenida',
	'2da Avenida',
	'3ra Avenida',
	'4ta Avenida',
	'5ta Avenida',
	'6ta Avenida',
]
# lista de zona
calle = [
	' 1ra calle',
	' 2da calle',
	' 3ra calle',
	' 4ta calle',
	' 5ta calle',
	' 6ta calle',
]
# lista de zona
zona =[
	' zona 15',
	' zona 10',
	' zona 11',
	' zona 12',
	' zona 13',
]
# lista de tiebda
tiendase = [
    ' la bendicion',
    ' eben-ezer',
    ' shaddai',
    ' la fe',
    ' sagrado corazon',
    ' jireh',
    ' el manatial',
    ' paiz',
    ' walmart',
    ' price-smart',
    ' club-co',
    ' uvg',
    ' samy store',
    ' Play store',
    ' Apple Store',
    ' ¡Shop',
    ' Steam'
]

# query para llenar la tabla de cliente
def query_cliente(id):
	nombre = random.choice(nameList)
	apellidos = random.choice(lastname)
	nombre_juntos = f'{nombre + apellidos}'
	#nit
	nit = random.randint(1000000,10000000)
	# credito 
	credito = random.randint(500,1000)
	datos = f'''
			INSERT INTO cliente VALUES(
				{id},
				{nit},
				'{nombre_juntos}',
				{credito}
			)
		'''
	c.execute(datos)
	return datos

# query para llenar la tabla de tienda
def query_tienda(id):
	# direcciones
	avenidas = random.choice(avenida)
	calles = random.choice(calle)
	zonas = random.choice(zona)
	direcciones = f'{avenidas + calles + zonas}'
	# random de tiendas
	tiendas = random.choice(tiendase)
	# f para castear los datos
	datosTiendas = f'''
			INSERT INTO tienda VALUES(
				{id},
				'{tiendas}',
				'{direcciones}'
			)
		'''
	c.execute(datosTiendas)
	return datosTiendas

# query para llenar la tabla de compras
def query_compras(id, tienda_id, cliente_id):
	total = random.randint(100,1000)
	dias = random.randint(1,30)
	mes = random.randint(1,12)
	ano = random.randint(2005,2019)
	fecha = f'{dias}/{mes}/{ano}'
	datosCompras = f'''
			INSERT INTO compra VALUES(
				{id},
				{cliente_id},
				{tienda_id}, 
				{total},
				'{fecha}'
			)
		'''
	c.execute(datosCompras)
	return datosCompras


if __name__ == '__main__':
	# ciclo para generar los datos los datos de la cantidad necesaria
	for i in range(1,1500):
		query_cliente(i)
		query_tienda(i)
	for i in range(1, 1500):
		query_compras(i+1, random.randint(1,500), random.randint(1,1500))

	conn.commit()
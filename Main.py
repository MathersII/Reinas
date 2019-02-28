from Nodo import Nodo
from Pila import Pila
import sys 

class Main(object):

	def  __init__(self):
		self.estado_inicial = self.conseguir_estado_inicial()
		#ruta = self.conseguir_ruta_iterativa(self.estado_inicial)
		ruta = self.conseguir_ruta_recursivamente(self.estado_inicial)[1]
		for x in ruta:
			self.imprime_matriz(x)


	def conseguir_ruta_recursivamente(self, estado, solucion = []):
		#self.imprime_matriz(estado.conseguir_tablero())
		if(self.es_solucion(estado) == False):
			solucion.insert(0,estado.conseguir_tablero())
			return (True,solucion)
		#Busqueda por profundidad (DFS)
		hijos = self.crear_hijos(estado)
		estado.set_hijos(hijos)
		while(len(estado.get_hijos()) > 0):
			if(self.conseguir_ruta_recursivamente(estado.get_hijo())[0]):
				solucion.insert(0,estado.conseguir_tablero())
				return (True,solucion)
		return (False,solucion)


	def conseguir_ruta_iterativa(self, estado):
		#Condiciones iniciales
		estado_actual = estado
		pila = Pila()
		visitados = []
		#Busqueda por profundidad (DFS)
		while(self.es_solucion(estado_actual)):
			visitados.append(estado_actual.conseguir_tablero())
			hijos = self.crear_hijos(estado_actual)
			for x in hijos:
				if x.conseguir_tablero() not in visitados:
					x.establecer_ruta_nodo(estado_actual.conseguir_ruta_nodo(), estado_actual.conseguir_tablero())
					pila.push(x)
			estado_actual = pila.pop()
		estado_actual.establecer_ruta_nodo(estado_actual.conseguir_ruta_nodo(), estado_actual.conseguir_tablero())
		return estado_actual.conseguir_ruta_nodo()

		 	
	def conseguir_estado_inicial(self):
		archivo_estado = open("estados.txt","r").read().split("\n")
		tablero = []
		for x in archivo_estado:
			tablero.append([int(y) for y in x.strip('\n').split(",")])
		tablero = self.llena_posiciones_prohibidas(self.busca_posiciones(tablero,2)[0],tablero)
		return Nodo(tablero)

	def crear_hijo(self, estado ):
		print ("Implementar método...")
		
	def crear_hermano(self, estado ):
		print ("Implementar método...")

	def crear_hijos(self, estado):
		Nodos = list(
			map(
				lambda x: Nodo(self.llena_posiciones_prohibidas(x,estado.conseguir_tablero())),self.busca_posiciones(estado.conseguir_tablero(),0)
				)
			) 
		return Nodos
		
	def busca_posiciones(self, tablero,num):
		lista = []
		for idxx, valx in enumerate(tablero):
			for idxy, valy in enumerate(valx):
				if valy == num :
					lista.append((idxx,idxy))
		return lista
					
	def llena_posiciones_prohibidas(self,posiciones,estado):
		tablero =  [x[:] for x in estado]
		x = posiciones[0]
		y = posiciones[1]
		tablero[x][y] = 2
		tablero = self.llena_fila_columna(tablero,x,y)
		tablero = self.llena_diag_ia(tablero,x,y)
		tablero = self.llena_diag_da(tablero,x,y)
		tablero = self.llena_diag_dab(tablero,x,y)
		tablero = self.llena_diag_iab(tablero,x,y)
		return tablero

	def llena_fila_columna(self,tablero,x,y):
		for i in range(0,8):
			if(tablero[x][i] != 2):
				tablero[x][i] = 1 
			if(tablero[i][y] != 2):
				tablero[i][y] = 1 
		return tablero	

	def llena_diag_ia(self,tablero,x,y):
		while x >= 0  and y >= 0 :
			if(tablero[x][y] != 2):
				tablero[x][y] = 1
			x = x - 1
			y = y - 1 
		return tablero

	def llena_diag_da(self,tablero,x,y):
		while x >= 0  and y < 8 :
			if(tablero[x][y] != 2):
				tablero[x][y] = 1
			x = x - 1
			y = y + 1 
		return tablero

	def llena_diag_dab(self,tablero,x,y):
		while x < 8  and y < 8:
			if(tablero[x][y] != 2):
				tablero[x][y] = 1
			x = x + 1
			y = y + 1 
		return tablero

	def llena_diag_iab(self,tablero,x,y):
		while x < 8  and y >= 0:
			if(tablero[x][y] != 2):
				tablero[x][y] = 1
			x = x + 1
			y = y - 1 
		return tablero

	def imprime_matriz(self,matriz):
		for x in matriz:
			for y in x:
				print(y, end="", flush=True)
			print('\n')
		print('\n\n')

	def es_solucion(self, estado_actual):
		tablero = estado_actual.conseguir_tablero()
		contador = 0
		for x in tablero:
			for y in x:
				if y == 2 :
					contador = contador+1
		if  contador == 8:
			return False
		else:
			return True
			

	def pruebas(self):
		print  ("=== pruebas main ===")
		estado_actual = self.conseguir_estado_inicial()
		self.imprime_matriz(estado_actual.conseguir_tablero())
		hijos = self.crear_hijos(estado_actual)
		for x in hijos:
			self.imprime_matriz(x.conseguir_tablero())
		
if __name__ == '__main__':
	main = Main()




		
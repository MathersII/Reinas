from Nodo import Nodo
from Pila import Pila
import sys
import copy 

class Main(object):

	def  __init__(self):
		self.visitados = []
		self.index = 0
		self.estado_inicial = self.conseguir_estado_inicial()
		ruta = self.conseguir_ruta(self.estado_inicial)
		for x in ruta.conseguir_ruta_nodo():
			self.imprime_matriz(x)
		#self.imprime_matriz(ruta.conseguir_tablero())
		
		self.pruebas()


	def conseguir_ruta(self, estado):
		
		#Condiciones iniciales
		estado_actual = estado
		pila = Pila()
		visitados = []

		#Busqueda por profundidad (DFS)
		while(self.es_solucion(estado_actual)):
			visitados.append(estado_actual.conseguir_tablero())
			hijos = self.crear_hijos(estado_actual)
			if len(hijos) != 0:
				for x in hijos:
					if x.conseguir_tablero() not in visitados:
						x.establecer_ruta_nodo(estado_actual.conseguir_ruta_nodo(), estado_actual.conseguir_tablero())
						pila.push(x)

			estado_actual = pila.pop()
		estado_actual.establecer_ruta_nodo(estado_actual.conseguir_ruta_nodo(), estado_actual.conseguir_tablero())
		return estado_actual

	def crear_hijos(self, estado):
		posiciones = []
		posiciones = self.busca_posiciones(estado)
		if posiciones != -1:
			Nodos = list(
				map(
					lambda x: Nodo(self.llena_posiciones_prohibidas(x,estado.conseguir_tablero())),posiciones
					)
				)
			return Nodos
		else:
			return []

	def busca_posiciones(self, estado,lista = []):
		lista = []
		for idxx, valx in enumerate(estado.conseguir_tablero()):
			for idxy, valy in enumerate(valx):
				if valy == 0 :
					lista.append((idxx,idxy))

		if len(lista) == 0:
			return -1
		return lista
					
	def llena_posiciones_prohibidas(self,posiciones,estado):
		tablero =  copy.deepcopy(estado)
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
		print('\n\n\n')

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
			
	def conseguir_estado_inicial(self):
		archivo_estado = open("estados.txt","r").read().split("\n")
		tablero = []
		for x in archivo_estado:
			tablero.append([int(y) for y in x.split(",")])
		return Nodo(tablero)

	def pruebas(self):
		print  ("=== pruebas main ===")



if __name__ == '__main__':
	main = Main()




		
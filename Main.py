from Nodo import Nodo
from Pila import Pila
import sys 

class Main(object):

	def  __init__(self):
		self.estado_inicial = self.conseguir_estado_inicial()
		ruta=self.conseguir_ruta()

	def conseguir_ruta(self, estado):
		#condiciones iniciales del problema
		estado_actual= estado

		#Busqueda por profundidad (DFS)
		while (es_solucion(estado_actual.conseguir_tablero())):
		 	hijo= crear_hijo(estado_actual)
		 	if hijo != 0:

		 		estado_actual=self.conseguir_ruta(hijo)
		 	else:
		 		estado_actual= self.crear_hermano(estado_actual)
		return estado_actual
		 	
	def crear_hijo(self, estado ):
		print ("Implementar método...")
		
	def crear_hermano(self, estado ):
		print ("Implementar método...")

	def es_solucion(self, estado_actual):
		contador = 0
		for x in estado_actual:
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






		
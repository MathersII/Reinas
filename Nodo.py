class Nodo:
	def __init__(self, lista):
		self.lista=lista
		self.ruta_al_nodo= []

	def conseguir_tablero(self):
		return self.lista
	def conseguir_ruta_nodo(self):
		return self.ruta_al_nodo
	def establecer_ruta_nodo(self, ruta , tablero):
		self.ruta_al_nodo= ruta+[tablero]


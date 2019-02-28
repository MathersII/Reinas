class Pila:
	def  __init__(self):
		self.lista=[]
	def push(self, elemento):
		self.lista.append(elemento)
	def pop(self):
		return self.lista.pop()
	def esVacio(self):
		return len(self.lista)==0

class Persona:
	
	def __init__(self, nombre):
		self.nombre = nombre
		self.habilidades = []
	
	def agregarHabilidades(self, habilidad):
		self.habilidades.append(habilidad) 
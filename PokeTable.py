from Pokemon import *

class PokeTable:
	def __init__(self):
		self.table = [[], [], []]

	def hashCode(self, name):
		code = len(name) % 3
		return code

	def insert(self, pokemon):
		hash = self.hashCode(pokemon.name)
		self.table[hash].append(pokemon)

	def remove(self, pokemon):
		hash = self.hashCode(pokemon.name)
		self.table[hash].remove(pokemon)

	def getPkm(self, name):
		name = name.lower()
		hash = self.hashCode(name)
		list = self.table[hash]

		for pokemon in list:
			if pokemon.name.lower() == name:
				return pokemon
		return False

	def showTable(self):
		counterA = 0
		for line in self.table:
			print(f'list[{counterA}]')
			counterB = 0
			for column in line:
				print(f'    {counterB}. {column.name} - {column.id}')
				counterB += 1
			print()
			counterA += 1

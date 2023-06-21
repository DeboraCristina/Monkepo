from PokeTable import PokeTable
from Pokemon import Pokemon


class Controller:
	def __init__(self, fileName):
		self.__fileName = fileName 
		self.lines = self.__openFile()
		pass
	
	def __openFile(self):
		cleanLines = []
		with open(
				self.__fileName, 'r') as readFile:
			lines = readFile.read()
		lines = lines.split('\n')
		for line in lines:
			if len(line) > 0 and line[0].isdigit():
				cleanLines.append(line)
		return cleanLines
	
	def getNames(self):
		names = []
		for line in self.lines:
			content = line.split(";")
			names.append(content[1].lower())
		return names

	def mountHashTable(self):
		table = PokeTable()
		for line in self.lines:
			pokemon = Pokemon(line)
			table.insert(pokemon)
		return table

	@staticmethod
	def getSimilarNames(name_to_find, all_names):
		found_names = []

		for name in all_names:
			if name_to_find in name:
				found_names.append(name)

		return found_names

class PokemonController:
	def __init__(self):
		pass
	
	def equals(self, pkmA, pkmB):
		nameA = pkmA.name.lower
		nameB = pkmB.name.lower
		return nameA == nameB

	def getRandom(self, id, allNames, hashTable):
		name = allNames[id]
		pkm = hashTable.getPkm(name)
		return pkm

	def isValidName(self, name, names):
		name = name.lower()
		if name in names:
			return True
		return False

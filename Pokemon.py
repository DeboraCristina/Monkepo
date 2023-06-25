class Pokemon:
	def __init__(self, content):
		content = content.split(';')
		self.id = content[0]
		self.name = content[1]
		self.types= self.getTypes(content[2])
		self.height = content[3]
		self.weight = content[4]
	
	def getTypes(self, content):
		if "/" in content:
			return content.split("/")
		return [content, content]

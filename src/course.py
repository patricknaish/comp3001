#!/usr/bin/python

class course:
	moduleList = []
	
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name

	def addModule(self, module):
		self.moduleList.append(module)
	
	def listModules(self):
		return '\n'.join(map(str, self.moduleList))
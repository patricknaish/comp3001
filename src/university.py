#!/usr/bin/python

class university:
	moduleList = []
	
	def __init__(self, name):
		self.name = name
		
	def addModule(self, module):
		self.moduleList.append(module)

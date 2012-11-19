#!/usr/bin/python

class Course:
    moduleList = []
    
    def __init__(self, courseID, name):
        self.name = name
        self.courseID = courseID
    
    def __str__(self):
        return self.name

    def addModule(self, module):
        self.moduleList.append(module)
    
    def listModules(self):
        return '\n'.join(map(str, self.moduleList))
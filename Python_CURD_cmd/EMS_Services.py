from Employee import *
class EMS_Services():
	emplist = []
	@classmethod
	def addEmployee(cls,emp):
		result = False
		e=cls.searchById(emp.getId())
		if (e != None):
			return False
		else:
			cls.emplist.append(emp)
			return True
		if (e.getId()==emp.getId()):
			return result
			
	@classmethod
	def getAllEmployee(cls):
		return cls.emplist
	
	@classmethod	
	def searchById(cls,id):
		for e in cls.emplist :
			if(e.getId()==id):
				return e
		return None
	@classmethod		
	def deleteById(cls,id):
		emp = cls.searchById(id)
		if (emp == None):
			return False
		else:
			cls.emplist.remove(emp)
			return True
		
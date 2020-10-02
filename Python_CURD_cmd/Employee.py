class Employee:
	
	def __init__(self,id=0,name=0,salary=0,address=0):
		self.__id = id
		self.__name = name
		self.__salary =  salary
		self.__address = address
		
	def __str__(self):
		return str(self.__id)+" "+str(self.__name)+" "+str(self.__salary)+"  "+str(self.__address)
		
	def getId(self):
		return self.__id
	def setId(self,id):
		self.__id=id
	def getName(self):
		return self.__name
	def setName(self,name):
		self.__name=name
		
	def getSalary(self):
		return self.__salary
	def setSalary(self,salary):
		self.__salary=salary
		
	def getAddress(self):
		return self.__address
	def setAddress(self,address):
		self.__address=address
		
'''if __name__ == "__main__":
o1=Employee(163,'pawa',100,'dummy')
print(o1)
print(o1.getId())
print(o1.getName())
print(o1.getSalary())
print(o1.getAddress())
o1.setId(153)
o1.setName('avi')
o1.setSalary(200)
o1.setAddress('tcs')
print(o1)'''

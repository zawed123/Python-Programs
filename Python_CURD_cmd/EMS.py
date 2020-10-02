from Employee import *
from EMS_Services import EMS_Services
if __name__=="__main__":
	while(True):
		print("1. Add Record: ")
		print("2. View All: ")
		print("3. Search By ID: ")
		print("4. Delete By ID: ")
		print("5. Exit ")
		
		choice = int(input("Enter Your Choice From 1-5 "))
		if (choice==1):
			emp=Employee()
			emp.setId(input("Enter ID: "))
			emp.setName(input("Enter NAME: "))
			emp.setSalary(input("Enter SALARY: "))
			emp.setAddress(input("Enter ADDRESS: "))
			if (EMS_Services.addEmployee(emp)):
				print("Record Inserted")
			else:
				print("Id Already Exists")
		elif (choice==2):
			lst = EMS_Services.getAllEmployee()
			if(len(lst)==0):
				print("No Record")
			else:
				for e in lst:
					print(e)
		elif (choice==3):
			id = input("Enter id : ")		
			emp = EMS_Services.searchById(id)
			if(emp==None):
				print("No Such Id Exists.")
			else:
				print(emp)
		elif (choice==4):
			id = int(input("Enter id : "))
			if(EMS_Services.deleteById(id)):
				print("Record Deleted")
			else:
				print("No Such Id Present")
		elif (choice==5):
			pass
		elif (choice==6):
			pass
		elif (choice==7):
			pass
		elif (choice==8):
			pass
		elif (choice==9):
			print("Thanks")
			break
		else:
			print("No Operation Present Here Related To Your Input")
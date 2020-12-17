EID=input("Enter Employee No:")
ENAME=input("Enter Employee Name:")
Age=input("Enter Age of Employee:")
ESALORY=input("Enter Employee Salory:")
EMS=input("Employee marriage status:")
employee_list=[]
employee_list.append(EID)
employee_list.append(ENAME)
employee_list.append(ESALORY)
employee_list.append(EMS)
employee_list.append(Age)
eligible='minor' if int(employee_list[4])<=18 else 'major'
print(employee_list[1],"is",eligible)

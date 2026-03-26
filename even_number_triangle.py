name=input("Enter the employee name: ")
id_e=int(input("Enter the employee id:"))
dept=input("Enter the employee department:")
basic_salary=float(input("Enter the basic salary: "))
da=0.92*basic_salary
hra=0.58*basic_salary
ta=0.30*basic_salary
lic=500
gross=basic_salary+da+hra+ta
net=gross-lic
print("Gross salary: ",gross)
print("Net salary: ",net)

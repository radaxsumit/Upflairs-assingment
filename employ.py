import manager 

print(manager.assistant_namee)
print(manager.assistant_idd)
print(manager.assistant_passe)

print(manager.manager_id)
print(manager.manager_name)
print(manager.manager_pass)

from manager import assistant_idd,assistant_namee
print(assistant_namee)
print(assistant_idd)

from manager import  assistant_name,assistant_id,assistant_pass
from manager import empolyee_data
from manager import max_salary_finder , employe_salary

max_salary_finder(employe_salary)
print("Employee file exicuted")
empolyee_data()


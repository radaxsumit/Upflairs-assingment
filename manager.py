## empolye records
empolyee = ['google','intel','microsoft','apple']

assistant_name = 'sundar pichu'
assistant_id = 'sundarpichu@gmail.cpom'
assistant_pass = 'sundar_pichu123'

employe_salary =[1000,2000,3000,4000] ## ----list of employee salaries

def max_salary_finder(employe_salary):  ##----creating function to find max salary
    if not employe_salary:
        return None
    max_salary = employe_salary[0]
    for salary in employe_salary:
        if salary > max_salary:
            max_salary = salary
    return max_salary
    
max_salary = max_salary_finder(employe_salary)
if max_salary is not None:
    print(f"The maximum salary among employe is : {max_salary}")
else:
    print("The list of max.salary is EMPTY!!!")


def empolyee_data():
    print("Your empolye list : ",empolyee)
    print("Your assistant name : ",assistant_name)
    print("Your assistant id : ",assistant_id)
    print("Your assistant pass : ",assistant_pass)


## Manager
print("Outside the condition ")
if __name__ =="__manager__":
    print("Inside the condition ")
    manager_name = "Sumit prajapati"
    manager_id = "Sumit@gmail.com"
    manager_pass = "hello123"

    def manger_data():
        print(manager_name)
        print(manager_id)
        print(manager_pass)

# print(__name__)
# empolyee_data()
# manger_data()

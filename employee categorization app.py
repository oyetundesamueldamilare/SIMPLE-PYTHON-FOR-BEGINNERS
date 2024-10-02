#2nd Sample nested list of employee names and their ages

employees = []
employee_count = int(input("enter number of employees"))

# Lists to store categorized employees
young_employees = []
middle_aged_employees = []
senior_employees = []

while employee_count != 0 :
    employee_count -=1
    name= str(input('what is your name?'))
    age = int(input('what is your age'))
    employees.append([name, age])
for employee in employees:
    name, age = employee
    if age < 30:
        young_employees.append(name)
    elif 30 <= age <= 50:
        middle_aged_employees.append(name)
    else:
        senior_employees.append(name)

# Print the categorized lists
print("Young Employees:", young_employees)
print("Middle-aged Employees:", middle_aged_employees)
print("Senior Employees:", senior_employees)
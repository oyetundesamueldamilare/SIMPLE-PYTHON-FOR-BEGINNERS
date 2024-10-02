#Employee categorizer based on age

def categorize_employees(employees):
    young_employees = [employee[0] for employee in employees if employee[1] < 30]
    middle_aged_employees = [employee[0] for employee in employees if 30 <= employee[1] <= 50]
    senior_employees = [employee[0] for employee in employees if employee[1] > 50]
    
    return young_employees, middle_aged_employees, senior_employees


def main():
    num_employees = int(input("Enter number of employees: "))
    
    if num_employees >=1 :
        employees = []
        for i in range(num_employees):
            name = input(f"Enter employee {i+1} name: ")
            age = int(input(f"Enter employee {i+1} age: "))
            employees.append([name, age])
        
        young, middle_aged, senior = categorize_employees(employees)
        
        print("\nEmployee Categorization by Age:")
        print("---------------------------")
        print("Young Employees (<30):", young)
        print("Middle-Aged Employees (30-50):", middle_aged)
        print("Senior Employees (50+):", senior)
    else:
        print("Invalid number of employees.")

if __name__ == "__main__":
    main()

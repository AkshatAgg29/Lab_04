class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self, employees):
        self.employees = employees

    def search_by_age(self, age):
        results = [emp for emp in self.employees if emp.age == age]
        return results

    def search_by_name(self, name):
        results = [emp for emp in self.employees if emp.name == name]
        return results

    def search_by_salary(self, operator, value):
        if operator == '>':
            results = [emp for emp in self.employees if emp.salary > value]
        elif operator == '<':
            results = [emp for emp in self.employees if emp.salary < value]
        elif operator == '>=':
            results = [emp for emp in self.employees if emp.salary >= value]
        elif operator == '<=':
            results = [emp for emp in self.employees if emp.salary <= value]
        else:
            results = []
        return results

def main():
    employees = [
        Employee('161E90', 'Raman', 41, 56000),
        Employee('161F91', 'Himadri', 38, 67500),
        Employee('161F99', 'Jaya', 51, 82100),
        Employee('171E20', 'Tejas', 30, 55000),
        Employee('171G30', 'Ajay', 45, 44000)
    ]
    
    db = EmployeeDatabase(employees)
    
    print("Choose search parameter:")
    print("1. Age\n2. Name\n3. Salary (>, <, <=, >=)")
    choice = int(input())
    
    if choice == 1:
        age = int(input("Enter age: "))
        results = db.search_by_age(age)
    elif choice == 2:
        name = input("Enter name: ")
        results = db.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (> / < / <= / >=): ")
        value = int(input("Enter salary value: "))
        results = db.search_by_salary(operator, value)
    else:
        print("Invalid choice.")
        return
    
    if not results:
        print("No matching records found.")
    else:
        print("Matching records:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()

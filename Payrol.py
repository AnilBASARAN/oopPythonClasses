class Programmer:
    
     # Add the class attributes
    salary = 100000
    monthly_bonus = 1000

    def __init__(self, name, age, address, phone, programming_languages):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages
 
 
class Assistant:
    salary = 40000
    monthly_bonus = 1000
    # Add the class attributes
    
    def __init__(self, name, age, address, phone, is_bilingual):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.is_bilingual = is_bilingual
 
 
# Function that prints the monthly salary of each worker
# and the total amount that the startup owner has to pay per month.
def calculate_payroll(employees):
 
    total = 0
 
    print("\n========= Welcome to our Payroll System =========\n")
 
    # Iterate over the list of instances to calculate
    # and display the monthly salary of each employee,
    # and add the monthly salary to the total for this month.
    for employee in employees:
        salary = round(employee.salary / 12, 2) + employee.monthly_bonus
        print(employee.name.capitalize() + "'s salary is: $" + str(salary))
        total += salary
 
    # Display the total
    print(f"\nWill This Work? The total payroll this month will be: $" +str(round(total,4)))


 
# Instances (employees)
jack = Programmer("Jack", 45, "5th Avenue", "555-563-345", ["Python", "Java"])
isabel = Programmer("Isabel", 25, "6th Avenue", "234-245-853", ["JavaScript"])
nora = Assistant("Nora", 23, "7th Avenue", "562-577-333", True)
 
# List of instances
employees = [jack, isabel, nora]
 
# Function call (Passing the list of instances as argument)
calculate_payroll(employees)
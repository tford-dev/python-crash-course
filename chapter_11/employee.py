"""
11-3. Employee: Write a class called Employee. The __init__() method should take in a first
name, a last name, and an annual salary, and store each of these as attributes. Write a method
called give_raise() that adds $5,000 to the annual salary by default but also accepts a different
raise amount.
"""
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name;
        self.last_name = last_name;
        self.annual_salary = annual_salary;
    
    def give_raise(self, amount=5000):
        self.annual_salary += amount
        return f"Employee {self.first_name.title()} {self.last_name.title()} has a salary of ${int(self.annual_salary)}."
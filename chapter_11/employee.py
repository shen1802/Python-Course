class Employee:
    """ A class that represents an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary=5000):
        """Method that increases the salary"""
        self.annual_salary += salary

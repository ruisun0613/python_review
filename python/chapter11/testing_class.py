"""
11-3. Employee: Write a class called Employee. The __init__() method
should take in a first name, a last name, and an annual salary, and store
each of these as attributes. Write a method called give_raise() that adds
$5,000 to the annual salary by default but also accepts a different raise
amount.
Write a test file for Employee with two test functions,
test_give_default_raise() and test_give_custom_raise(). Write your tests once
without using a fixture, and make sure they both pass. Then write a fixture
so you don’t have to create a new employee instance in each test function.
Run the tests again, and make sure both tests still pass.
"""
class Employee:
    def __init__(self, f_name, l_name, annual_salary):
        self.first_name = f_name
        self.last_name = l_name
        self.salary = annual_salary


    def give_raise(self, amount=5000):
        self.salary += amount
        return self.salary

# employee = Employee("Rui", "Sun", 55000)
# print(employee.first_name, employee.last_name, employee.salary)
# new_salary = employee.give_raise()
# print(new_salary)
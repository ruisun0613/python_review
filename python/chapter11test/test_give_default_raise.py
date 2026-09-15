from python.chapter11.testing_class import Employee

def test_give_default_raise():
    employee = Employee("Rui", "Sun", 55000)
    employee.give_raise()
    assert employee.salary == 60000

def test_give_custom_raise():
    employee = Employee("Rui", "Sun", 55000)
    employee.give_raise(10000)
    assert employee.salary == 65000


# Using fixture
import pytest

@pytest.fixture
def employee():
    return Employee("Rui", "Sun", 60000)

def test_employee(employee):
    new_employee = employee

    new_employee.give_raise()

    assert new_employee.salary == 65000
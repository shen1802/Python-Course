import pytest

from chapter_11.employee import Employee


@pytest.fixture
def employee():
    """An employee object"""
    employee = Employee('adam', 'adamou', 10000)
    return employee


def test_give_default_raise(employee):
    """Test the default salary raise"""
    employee.give_raise()
    assert employee.annual_salary == 15000


def test_give_custom_raise(employee):
    """Test the custom salary raise"""
    employee.give_raise(1000)
    assert employee.annual_salary == 11000

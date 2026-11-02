"""Это docstring модуля test_employee_by_id.py."""
import pytest

# from app.company import employees
from app.utils import get_employee_by_id

def test_get_employee_by_id(employees):
    assert get_employee_by_id(employees, 1)["name"] == "Иван Петров"
    assert get_employee_by_id(employees, 1)["department"] == "IT"
    assert get_employee_by_id(employees, 1)["age"] == 28
    assert get_employee_by_id(employees, 1)["hire_year"] == 2021
    assert get_employee_by_id(employees, 1)["fire_year"] is None
    assert get_employee_by_id(employees, 1)["history"][0]["year"] == 2023
    assert get_employee_by_id(employees, 1)["history"][0]["salary"] == 3900
    assert get_employee_by_id(employees, 1)["history"][0]["projects"] == 4 

    assert get_employee_by_id(employees, 8)["name"] == "Елена Белова"
    assert get_employee_by_id(employees, 8)["department"] == "Finance"
    assert get_employee_by_id(employees, 8)["age"] == 46
    assert get_employee_by_id(employees, 8)["hire_year"] == 2015
    assert get_employee_by_id(employees, 8)["fire_year"] == 2024
    assert get_employee_by_id(employees, 8)["history"][1]["year"] == 2024
    assert get_employee_by_id(employees, 8)["history"][1]["salary"] == 4500
    assert get_employee_by_id(employees, 8)["history"][1]["projects"] == 2

    assert get_employee_by_id(employees, 999) not in employees 
    print("Все тесты успешно пройдены")
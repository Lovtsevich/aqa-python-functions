import pytest
from app.company import employees
from app.utils import get_department_employees

def test_get_department_employees():
    department_hr = get_department_employees(employees, "HR")
    assert len(department_hr) > 0
    assert all(emp["department"] == "HR" for emp in department_hr)

    department_it = get_department_employees(employees, "IT")
    assert len(department_hr) > 0
    assert all(emp["department"] == "IT" for emp in department_it)
   
    print("Все тесты успешно пройдены")
# """Это docstring модуля test_active_employees.py."""
import pytest

from app.company import employees
from app.utils import get_active_employees

# # # Проверка поиска по employee_id
def test_get_active_employees():
    assert len(get_active_employees(employees)) > 0

    print("Все тесты успешно пройдены")
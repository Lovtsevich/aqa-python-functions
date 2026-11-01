import pytest

from app.utils import get_fired_employees

def test_get_fired_employees(employees):
    assert len(get_fired_employees(employees)) > 0

    print("Все тесты успешно пройдены")
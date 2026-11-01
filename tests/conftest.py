import pytest

@pytest.fixture
def employees():
    return [
        {
                "id": 1,
                "name": "Иван Петров",
                "department": "IT",
                "age": 28,
                "hire_year": 2021,
                "fire_year": None,
                "history": [
                    {"year": 2023, "salary": 3900, "projects": 4},
                    {"year": 2024, "salary": 4300, "projects": 5},
                    {"year": 2025, "salary": 4700, "projects": 6},
                    {"year": 2026, "salary": 5200, "projects": 7}
                ]
            },
        {
                "id": 8,
                "name": "Елена Белова",
                "department": "Finance",
                "age": 46,
                "hire_year": 2015,
                "fire_year": 2024,
                "history": [
                    {"year": 2023, "salary": 4300, "projects": 3},
                    {"year": 2024, "salary": 4500, "projects": 2}
                ]
            }
    ]
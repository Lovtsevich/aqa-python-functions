"""Это docstring модуля utils.py."""
# Поиск сотрудников. Вернуть сотрудника по ID.
def get_employee_by_id(employees, employee_id):
    """Это docstring функции get_employee_by_id"""
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None

# Список работающих сотрудников
def get_active_employees(employees):
    """
    сотрудник работает в компании если:
    - fire_year == None 
    """
    list_active_employees = []
    for employee in employees:
        if employee["fire_year"] is None:
            list_active_employees.append(employee)
    return list_active_employees

# Вернуть список уволенных сотрудников.
def get_fired_employees(employees):
    list_fired_employees = []
    for employee in employees:
        if employee["fire_year"] is not None:
            list_fired_employees.append(employee)
    return list_fired_employees



# Вернуть список сотрудников указанного отдела.

def get_department_employees(employees, department):
    list_department_employees = []
    for employee in employees:
        if employee["department"] == department:
            list_department_employees.append(employee)
    return list_department_employees

# ---

# ```python
# def get_hired_after(employees, year):
# ```

# Вернуть список сотрудников, принятых после указанного года.

# ---

# ```python
# def get_older_than(employees, age):
# ```

# Вернуть список сотрудников старше указанного возраста.

# ---

# ## Работа с историей сотрудника

# ```python
# def get_salary_by_year(employee, year):
# ```

# Вернуть зарплату сотрудника за указанный год.

# Если год отсутствует, вернуть:

# ```python
# None
# ```

# ---

# ```python
# def get_projects_by_year(employee, year):
# ```

# Вернуть количество проектов сотрудника за указанный год.

# Если год отсутствует, вернуть:

# ```python
# None
# ```

# ---

# ```python
# def get_average_salary(employee):
# ```

# Вернуть среднюю зарплату сотрудника за все годы.

# ---

# ```python
# def get_max_salary(employee):
# ```

# Вернуть максимальную зарплату сотрудника.

# ---

# ```python
# def get_total_salary(employee):
# ```

# Вернуть суммарную зарплату сотрудника за все годы.

# ---

# ```python
# def get_total_projects(employee):
# ```

# Вернуть суммарное количество проектов сотрудника за все годы.

"""
filename: employees_manager.py
author: alexbozhinov
created: 20.01.2023
purpose: definition of class EmployeesManager, which inherits RecruitmentManager and SalaryManager
"""
from model.management.recruitment_manager import RecruitmentManager
from model.management.salary_manager import SalaryManager


class EmployeesManager(RecruitmentManager, SalaryManager):
    pass

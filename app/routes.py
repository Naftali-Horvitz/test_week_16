from fastapi import APIRouter
from dal import *

router = APIRouter()

@router.get("/employees/engineering/high-salary")
def engineering_high_salary_employees():
    try:
        return get_engineering_high_salary_employees()
    except Exception as e:
        raise e
    
@router.get("/employees/by-age-and-role")
def employees_by_age_and_role():
    try:
        return get_employees_by_age_and_role()
    except Exception as e:
        raise e

@router.get("/employees/top-seniority")
def employees_top_seniority():
    try:
        return get_top_seniority_employees_excluding_hr()
    except Exception as e:
        raise e

@router.get("/employees/age-or-seniority")
def employees_age_or_seniority():
    try:
        return get_employees_by_age_or_seniority()
    except Exception as e:
        raise e

@router.get("/employees/managers/excluding-departments")
def employees_managers_excluding_departments():
    try:
        return get_managers_excluding_departments()
    except Exception as e:
        raise e

@router.get("/employees/by-lastname-and-age")
def employees_by_lastname_and_age():
    try:
        return get_employees_by_lastname_and_age()
    except Exception as e:
        raise e
from connection import get_col
import re
from fastapi import HTTPException

def get_engineering_high_salary_employees():
    try:
        mycol = get_col()
        projection = {'employee_id': 1, 'name': 1, 'salary': 1, '_id': 0}
        query = {'job_role.department': 'Engineering', 'salary':{'$gt': 65000}}
        res = mycol.find(query, projection).to_list()
        if not res:
            raise HTTPException(status_code=404, detail="employees not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"res": res}

def get_employees_by_age_and_role():
    try:
        mycol = get_col()
        projection = {'_id': 0}
        query = {'job_role.department': {'$in':['Engineering', 'Specialist']}, 'age':{'$gte': 30, '$lte': 45}}
        res = mycol.find(query, projection).to_list()
        if not res:
                raise HTTPException(status_code=404, detail="employees not found")
        return {"res": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_top_seniority_employees_excluding_hr():
    try:
        mycol = get_col()
        projection = {'_id': 0}
        query = {'job_role.department': {'$ne': 'HR'}}
        res = mycol.find(query, projection).sort({'years_at_company' : -1}).limit(7).to_list()
        if not res:
            raise HTTPException(status_code=404, detail="employees not found")
        return {"res": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_employees_by_age_or_seniority():
    try:
        mycol = get_col()
        projection = {'_id': 0, 'employee_id': 1, 'name': 1, "age": 1, 'years_at_company' : 1}
        query = {'$or':[{'age': {'$gt': 50}}, {'years_at_company': {'$lt': 3}}]}
        res = mycol.find(query, projection).to_list()
        if not res:
            raise HTTPException(status_code=404, detail="employees not found")
        return {"res": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_managers_excluding_departments():
    try:
        mycol = get_col()
        projection = {'_id': 0}
        query = {'job_role.title': 'Manager','job_role.department': {'$nin':['Sales', 'Marketing']}}
        res = mycol.find(query, projection).to_list()
        if not res:
            raise HTTPException(status_code=404, detail="employees not found")
        return {"res": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def get_employees_by_lastname_and_age():
    try:
        mycol = get_col()
        projection = {'_id': 0, 'name': 1, "age": 1, 'job_role.department' : 1}
        query = {'age': {'$lt': 35}, 'name': {'$in':[re.compile("Nelson$"), re.compile("Wright$")]}}
        res = mycol.find(query, projection).to_list()
        if not res:
            raise HTTPException(status_code=404, detail="employees not found")
        return {"res": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
       

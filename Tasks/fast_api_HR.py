from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from fastapi import FastAPI

app = FastAPI()


@app.get("/employees")
def read_root():
    # engine = create_engine('mysql://root:root@localhost:3306/newschema')
    # with engine.connect() as con:
    #     query = 'SELECT first_name, last_name FROM employees;'
    #     res = con.execute(text(query))
    # print(res)
    return "Hello"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/main")
def read_main():
    return "This is main page! Why not)"

from sqlalchemy import create_engine
from sqlalchemy.sql import text

"""
TASK 1
"""
engine = create_engine('mysql://root:root@localhost:3306/newschema')

with engine.connect() as con:
    query = 'SELECT first_name, last_name FROM employees;'
    res = con.execute(text(query))
    for row in res:
        print(row)

"""
TASK 2
"""

with engine.connect() as con:

    statement = text("""INSERT INTO employees(first_name, last_name, job_id, salary) 
    VALUES(:first_name, :last_name, :job_id, :salary)""")

    statement_new = text("""INSERT INTO employees(first_name, last_name, job_id, salary) 
    VALUES('Maxim', 'Kostenko', 'ST_MAN', '8000')""")

    data_ = con.execute(statement_new)
    print(data_)

    # print(type(data))
    # con.execute(statement, **data)

"""
TASK 3
"""
'''Необходимо создать API для управления списком задач. Каждая задача должна содержать заголовок и описание. Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. Для этого использовать библиотеку Pydantic.'''

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from flask import Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./HW_5/templates")

tasks = []


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool = False


@app.get('/task', response_class=HTMLResponse)
async def show_tasks(request: Request):
    table = pd.DataFrame([vars(task) for task in tasks]).to_html()
    return templates.TemplateResponse('task_HW_5.html', {"request":request,"table":table})

@app.get('/task/{task_id}', response_class=HTMLResponse)
async def show_task(request: Request,task_id:int):
    task = pd.DataFrame([vars(my_task) for my_task in tasks if my_task.id ==- task_id]).to_html(index=False)
    return templates.TemplateResponse('task_HW_5.html', {"request":request,"task":task})

@app.post("/task", response_model=Task)
async def create_task(task: Task):
    task_id = len(tasks) + 1
    task.id = task_id
    tasks.append(task)
    return task


@app.put("/task/{task_id}", response_class=Task)
async def put_task(task_id:int, task: Task):
    for i, new_task in enumerate(tasks):
        if new_task.id == task_id:
            task.id = task_id
            tasks[i] = task
            return task


@app.delete("/task/{task_id}", response_class=Task)
async def delete_task(task_id:int):
    for i, remove_task in enumerate(tasks):
        if remove_task.id == task_id:
            task_delete_table = pd.DataFrame([vars(tasks.pop(i))]).to_html()
            return task_delete_table

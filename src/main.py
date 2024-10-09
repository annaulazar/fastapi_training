from typing import Optional
from fastapi import FastAPI
import uvicorn

from src.utils import EducationLevel, SolarObjects, Tag

# Создание объекта приложения.
app = FastAPI(docs_url='/swagger')


@app.get('/me', tags=['common methods'], summary='Приветсвие автора')
def hello_author():
    return {'Hello': 'author'}


@app.get('/multiplication', tags=['special methods'], summary='Площадь прямоугольника или объем параллелограмма')
def multiplication(length: int, width: int, depth: Optional[int] = None) -> int:
    if depth is not None:
        return length * width * depth
    return length * width


@app.get('/get-solar-object-name', tags=['special methods'], summary='Название космического объекта по диаметру')
def get_solar_object_name(diameter: SolarObjects) -> str:
    return diameter.name


@app.get('/{name}', tags=['common methods'], summary='Общее приветсвие')
def greetings(name: str, surname: str, age: Optional[int] = None,
              is_staff: bool = False, education_level: Optional[EducationLevel] = None) -> dict[str, str]:
    """
        Приветствие пользователя:

        - **name**: имя
        - **surname**: фамилия
        - **age**: возраст (опционально)
        - **is_staff**: является ли пользователь сотрудником
        - **education_level**: уровень образования (опционально)
    """
    result = (" ".join([name, surname])).title()
    print(result)
    if age is not None:
        result += ', ' + str(age)
    if education_level is not None:
        result += ', ' + education_level.lower()
    if is_staff:
        result += ', сотрудник'

    return {'Hello': result}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)

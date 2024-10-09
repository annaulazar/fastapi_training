from fastapi import FastAPI
from enum import StrEnum

app = FastAPI()


class Tag(StrEnum):
    IMMUTABLE = 'immutable'
    MUTABLE = 'mutable'


@app.post('/a', tags=[Tag.IMMUTABLE], summary='Первая функция', response_description='Строка')
def a() -> str:
    """
    Функция возвращает ответ в виде строки
    """
    return 'Вот это ответ!'


@app.get('/b', tags=[Tag.MUTABLE], summary='Вторая функция', description='Ответ в виде массива строк',
         response_description='Массив строк')
def b() -> list[str]:
    return ['Вот', 'это', 'ответ!']


@app.post('/c', tags=[Tag.IMMUTABLE], summary='Третья функция', response_description='Число')
def c() -> int:
    """
    Функция возвращает одно число
    """
    return 42


@app.get('/d', tags=[Tag.MUTABLE], summary='Четвертая функция', description='Ответ в виде словаря',
         response_description='Словарь')
def d() -> dict[str, str]:
    return {'Вот': 'это ответ!'}

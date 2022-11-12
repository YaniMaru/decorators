# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)
import datetime
from functools import wraps
import time


def cacher(func):
    cach = {}

    @wraps(func)
    def wrapper(*args):
        key = args
        if key not in cach:
            cach[key] = func(*args)
        return cach[key]

    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'функция: {func.__name__}\t'
        log_msg += f"параметры: {', '.join(map(str, args))}\t"
        start = time.perf_counter_ns()
        res = func(*args, **kwargs)
        finish = time.perf_counter_ns() - start
        log_msg += f'результат: {res}\t'
        log_msg += f'Время выполнения: {finish}\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper






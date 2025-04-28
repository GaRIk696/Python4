# 1. Создайте список квадратов первых 10 натуральных чисел, используя list comprehension.
def sq_list_comp(num):
    return [(i+1)**2 for i in range(num)]

print("1.", sq_list_comp(10))

# 2. Создайте словарь, содержащий названия дней недели и их порядковые номера, используя dict comprehension.
# Для дней недели можно использовать список ["Понедельник", "Вторник" и т.д.]

def week_days(week_day=None):
    if week_day is None:
        week_day = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    return {day: i + 1 for i, day in enumerate(week_day)}

print(f"2. {week_days()}")

# 3. Создайте множество, содержащее теги библиотек в нижнем регистре, используя list comprehension.
# Исходный список ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

def mn_libs(libs=None):
    if libs is None:
        libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
    return {lib.lower() for lib in libs}

print(f"3. {mn_libs()}")
# 4. Создайте список, содержащий только четные числа из исходного списка, используя list comprehension.
# Исходный список [1, 3, 4, 87, 98, 15, 7, 4]

def cht_nums(nums=None):
    if nums is None:
        nums = [1, 3, 4, 87, 98, 15, 7, 4]
    return [x for x in nums if x % 2 == 0]

print(f"3. {cht_nums()}")

# 5. Создайте словарь, где ключи — это числа от 1 до 5, а значения — их факториалы, используя dict comprehension.
# Для вычисления факториала
# импортируйте функцию factorial из модуля math, либо реализуйте вычисление факториала самостоятельно.
def calc_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

factorials = {n: calc_factorial(n) for n in range(1, 6)}
print(f"5. {factorials}")
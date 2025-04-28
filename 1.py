from math import factorial

# 1. Список квадратов первых 10 натуральных чисел
squares = [x**2 for x in range(1, 11)]
print(f"1. {squares}")

# 2. Словарь дней недели с порядковыми номерами
week_days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
day_numbers = {day: idx+1 for idx, day in enumerate(week_days)}
print(f"2. {day_numbers}")

# 3. Множество тегов библиотек в нижнем регистре
libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
unique_tags = {lib.lower() for lib in libs}
print(f"3. {unique_tags}")

# 4. Список только четных чисел из исходного списка
nums = [1, 3, 4, 87, 98, 15, 7, 4]
even_nums = [num for num in nums if num % 2 == 0]
print(f"4. {even_nums}")

# 5. Словарь факториалов чисел от 1 до 5
fact_dict = {n: factorial(n) for n in range(1, 6)}
print(f"5. {fact_dict}")
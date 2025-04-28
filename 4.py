def decor(func):
    def wrapper(*args, **kwargs):
        print(f"Функция '{func.__name__}' вызвана с аргументами:")
        print(f"Позиционные аргументы (args): {args}")
        print(f"Именованные аргументы (kwargs): {kwargs}")

        res = func(*args, **kwargs)
        return res

    return wrapper

@decor
def calculate(length, width):
    try:
        length_num = float(length)
        width_num = float(width)

        if length_num <= 0 or width_num <= 0:
            raise ValueError("Длина и ширина должны быть положительными числами.")

        area = length_num * width_num
        return area
    except ValueError as e:
        return f"Ошибка: {e}"
length_input = input("Введите длину прямоугольника: ")
width_input = input("Введите ширину прямоугольника: ")

result = calculate(length_input, width_input)
print(f"Площадь прямоугольника: {int(result) if result % 2 == 0 else result }")
def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def prime_generator():
    yield 2
    num = 3
    while True:
        if is_prime(num):
            yield num
        num += 2


def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        print("Ошибка: введите положительное целое число.")


print("Генератор простых чисел")
print("-----------------------")

generator = prime_generator()
n = get_positive_integer("Введите количество простых чисел для вывода: ")

print(f"\nПервые {n} простых чисел:")
for _ in range(n):
    print(next(generator))
def nums():
    num = 2
    while True:
        is_num = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_num = False
                break
        if is_num:
            yield num
        num += 1

def get_nums():
    while True:
        inp = input("Введите количество простых чисел для вывода: ")
        if inp.isdigit() and int(inp) > 0:
            return int(inp)
        print("Ошибка: введите положительное целое число.")

numbers = nums()
n = get_nums()

for m in range(n):
    print(next(numbers))
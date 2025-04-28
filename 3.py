def append_to_file(text, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + '\n')

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print("Чётные строки файла:")
        for idx, line in enumerate(lines, start=1):
            if idx % 2 == 0:
                print(line.strip())

with open('example.txt', 'w', encoding='utf-8') as f1:
    f1.write("Первая строка\nВторая строка\nТретья строка\nЧетвертая строка\n")

append_to_file("Пятая строка", "example.txt")
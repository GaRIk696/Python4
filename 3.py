class Files:
    def __init__(self, text, filename):
        self.filename = filename
        self.text = text + '\n'

    def __enter__(self):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(self.text)
        return self

    def print_lines(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print("Чётные строки файла:")
            for idx, line in enumerate(lines, 1):
                if idx % 2 == 0:
                    print(f"{idx}: {line.strip()}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.print_lines()
        return False


initial_lines = [
    "Первая строка",
    "Вторая строка",
    "Третья строка",
    "Четвёртая строка",
    "Пятая строка"
]

new_filename = "example.txt"


with open(new_filename, 'w', encoding='utf-8') as file:
    file.write('\n'.join(initial_lines))

while True:
    user_text = input("Введите текст для добавления в файл (или 'exit' для выхода): ")
    if user_text.lower() == 'exit':
        break

    with Files(user_text, new_filename):
        pass
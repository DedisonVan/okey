with open('file1.txt') as file1, open('file2.txt') as file2:
    # читаем оба файла и сохраняем их содержимое в списки
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()

# удаляем начальные пробельные символы и переводим все символы в нижний регистр
file1_lines = [line.lstrip().lower() for line in file1_lines]
file2_lines = [line.lstrip().lower() for line in file2_lines]

# создаем множества из строк, чтобы убрать дубликаты
file1_set = set(file1_lines)
file2_set = set(file2_lines)

# находим уникальные строки в каждом файле и выводим их
file1_unique = file1_set - file2_set
file2_unique = file2_set - file1_set

print("Уникальные строки в файле 1:")
print(file1_unique)

print("Уникальные строки в файле 2:")
print(file2_unique)
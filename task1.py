file = open('names.txt', 'r')
file = file.read()

names = []
numbers = []
multiply = []
amount = 0
dict_of_names_and_numbers = {}

# add names separated by commas to list
# добавляем имена, разделённые запятыми, в список
spsk = file.split(',', -1)

# leave letters only
# оставляем тольк буквы
for name in spsk:
    names.append(name.replace('"', ''))

# sort our list
# сортируем список
names.sort()
print(f"Сортированный список выглядит так: {names}")

# count alphabet sum
# считаем алфавитную сумму
for name in names:
    value = 0
    for letter in name:
        value += ord(letter) - 64
    numbers.append(value)
print(f"Алфавитные суммы имён: {numbers}")

# add alphabet sums and names indexes multiply results in the list
# добавляем результаты умножения алфавитных сумм на порядковые номера имён в список
for i in range(len(names)):
    multiply.append(numbers[i] * (i+1))

# totalize results
# складываем результаты
for i in multiply:
    amount += i

# add a couples to the dict
# добавляем пары имя-алфавитная сумма в словарь
for i in range(len(names)):
    dict_of_names_and_numbers[names[i]] = numbers[i]

print(f"Словарь с именами и алфавитными суммами: {dict_of_names_and_numbers}")
print(f"Итоговая сумма: {amount}")

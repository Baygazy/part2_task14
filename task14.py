numbers = [int(number) for number in input('Введите числа через пробел: ').split()] #генератор списка
for num in numbers:
    if num % 2 == 0:
        print(num)
    else:
        continue


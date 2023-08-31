# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

ATTEMPT_COUNT = 10
count = 0
num = randint(0,1000)
def Compare(my_version_num, hidden_num):
    if my_version_num > hidden_num:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")
def Check(count, num):
    while (True):
        if count < ATTEMPT_COUNT:
            my_num = int(input("Введите число: "))
            if my_num == num:
                print("В точку!")
                return False
            else:
                count += 1
                Compare(my_num, num)
                Check(count, num)
                return True
        else:
            print("Попытки закончились, вы не угадали")
            return False
Check(count, num)
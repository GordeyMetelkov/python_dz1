from random import randint

ATTEMPT_COUNT = 10
low_limit = 0
up_limit = 20
count = 0
num = int(input("Введите число: "))
def Compare(machine_version_num, hidden_num, low_limit, up_limit):
    if machine_version_num > hidden_num:
        up_limit = machine_version_num
    else:
        low_limit = machine_version_num
def Check(count, num):
    while (True):
        if count < ATTEMPT_COUNT:
            print(f'"Попытка" {count + 1}')
            machine_version_num = randint(low_limit, up_limit)
            if machine_version_num == num:
                print("В точку!")
                return False
            else:
                print("Неудачно!")
                count += 1
                Compare(machine_version_num, num, low_limit, up_limit)
                Check(count, num)
                return True
        else:
            print("Попытки закончились, я не угадал")
            return False
if num <= up_limit:
    Check(count, num)
else:
    print("Число вне диапозона, попробуйте снова")
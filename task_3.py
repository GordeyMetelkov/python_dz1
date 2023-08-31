count = 2
num = int(input("Введите число: "))
if count >= num:
    print("Простое")
elif num == 0:
    print("Ноль ни простое, ни составное")
else:
    while count < num:
        if num % count == 0:
            print("Составное")
            break
        else:
            count += 1
            if count == num:
                print("Простое")
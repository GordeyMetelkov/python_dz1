#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
#Дано a, b, c - стороны предполагаемого треугольника.
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
#Если хотя бы в одном случае отрезок окажется больше суммы двух других,
#то треугольника с такими сторонами не существует.
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Введите сторону 'A': "))
b = int(input("Введите сторону 'B': "))
c = int(input("Введите сторону 'C': "))

if a + b <= c or a + c <= b or c + b <= a:
    print("Треугольника с такими сторонами не существует")
elif (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
    print("Треугольник равнобедренный")
elif a == b and a == c:
    print("Треугольник равноcторонний")
else:
    print("Треугольник равноcторонний")
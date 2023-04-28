# ВЫЧИСЛИТЬ A в СТЕПЕНИ B

def PowerRecursion(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * PowerRecursion(A, B - 1))
A = int(input("Введите число: "))
B = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", PowerRecursion(A, B))


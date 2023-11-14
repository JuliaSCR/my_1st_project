# задача 1 Посчитать сумму цифр любого целого или вещественного числа, число вводит пользователь.

def amount_digits():
    n = float(input("Введите любое число: "))
    result = 0
    if n % 1 != 0:
        while n % 1 != 0:
            n *= 10
        while n != 0:
            result += n % 10
            n //= 10
    else:
        while n != 0:
            result += n % 10
            n //= 10
    return result

print(amount_digits())

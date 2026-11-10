def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def main():
    print("КАЛЬКУЛЯТОР")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    print("Сложение:", add(a, b))
    print("Вычитание:", subtract(a, b))
    print("Умножение:", multiply(a, b))


if __name__ == "__main__":
    main()

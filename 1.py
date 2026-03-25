num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

product = num1 * num2
summa = num1 + num2
difference = num1 - num2

average = summa / 2

print("\nРезультаты вычислений:")
print(f"Произведение: {num1} * {num2} = {product}")
print(f"Сумма: {num1} + {num2} = {summa}")
print(f"Разница: {num1} - {num2} = {difference}")
print(f"Среднее арифметическое: ({num1} + {num2}) / 2 = {average}")
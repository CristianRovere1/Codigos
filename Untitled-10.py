numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
op = input("Digite qual operação (+, -, * ou /) deseja realizar: ")
if op == "+":
    resultado = numero1 + numero2
elif op == "-":
    resultado = numero1 - numero2
elif op == "*":
    resultado = numero1 * numero2
elif op == "/":
    resultado = numero1 / numero2
else:
    resultado = 0

print("\nO resultado é: ")


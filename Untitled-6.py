resposta=float(input('Qual a nota [0.0 - 10.0]: '))

if resposta < 6.0:
    print('Nota F')
elif resposta < 7.0:
    print('Nota D')
elif resposta < 8.0:
    print('Nota C')
elif resposta < 9.0:
    print('Nota B')
else:
    print('Nota A')
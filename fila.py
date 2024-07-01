fila = []
while True:
    print("Menu:")
    print("1. Entrar na fila")
    print("2. Atender cliente")
    print("3. Mostrar fila")
    print("4. Sair do programa")

    escolha = input("Escolha uma opção (1/2/3/4): ")

    if escolha == '1':
        cliente = input("Digite o nome do cliente: ")
        fila.append(cliente)
        print(f"{cliente} entrou na fila.")

    elif escolha == '2':
        if not fila:
            print("A fila está vazia.")
        else:
            cliente_atendido = fila.pop(0)
            print(f"{cliente_atendido} foi atendido.")

    elif escolha == '3':
        print("Fila de atendimento:")
        if not fila:
            print("Não há alguém para atender.")
        else:
            for index, cliente in enumerate(fila, start=1):
                print(f"{index}. {cliente}")
        print()

    elif escolha == '4':
        print("Turno encerrado, até amanhã!.")
        break

    else:
        print("Opção inválida, tente de novo (1/2/3/4).")

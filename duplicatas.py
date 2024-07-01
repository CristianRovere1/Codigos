elementos = input("Insira os elementos da lista separados por espaço: ").split()
elementos_sem_duplicatas = list(set(elementos))
print("Lista sem duplicatas:", elementos_sem_duplicatas)

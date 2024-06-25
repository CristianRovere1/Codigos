
lista1 = []
n1 = int(input("Quantos quantos itens pretendo colocar na lista "))
for i in range(n1):
    elemento = input(f"diga o Item {i+1}: ")
    lista1.append(elemento)


lista2 = []
n2 = int(input("Quantos itens serão colocados na segunda lista? "))
for i in range(n2):
    elemento = input(f"Informe o item {i+1}: ")
    lista2.append(elemento)


lista_concatenada = lista1 + lista2

# Mostrar a lista concatenada
print("Listas concatenadas:", lista_concatenada)
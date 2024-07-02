lista_palavras = ['gato', 'gelo', 'pato', 'peixe', 'rato', 'leito', 'biscoito', 'reitor', 'lateral', 'leitor']
letra_desejada = input("Digite a letra pela qual deseja filtrar as palavras: ")
print(f"Palavras que começam com '{letra_desejada}':")
for palavra in lista_palavras:
    if palavra.lower().startswith(letra_desejada.lower()):
        print(palavra)

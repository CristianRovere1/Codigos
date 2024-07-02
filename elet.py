
comidas = ['leite', 'couve', 'computador', 'tomate', 'garfo', 'faca', 'tablet', 'refrigerante']
bebidas = ['uva', 'colher', 'TV', 'vinho', 'cerveja', 'celular', 'banana']
talheres = ['arroz', 'iPhone', 'concha', 'whisky', 'vodka', 'feijão', 'colher de chá']

eletronicos = []

for item in comidas[:]:  
    if item.lower() in ['computador', 'tablet']:
        eletronicos.append(item)
        comidas.remove(item)

for item in bebidas[:]:  
    if item.lower() in ['tv', 'celular']:
        eletronicos.append(item)
        bebidas.remove(item)

for item in talheres[:]: 
    if item.lower() in ['iphone']:
        eletronicos.append(item)
        talheres.remove(item)

comidas.sort()
bebidas.sort()
talheres.sort()

print("Comidas:", comidas)
print("Bebidas:", bebidas)
print("Talheres:", talheres)
print("Eletrônicos:", eletronicos)

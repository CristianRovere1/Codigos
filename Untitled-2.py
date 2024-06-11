lista1 = ['Maçã', 'Garfo', 'Banana', 'Faca', 'Laranja']
lista2 = ['Colher', 'Pera', 'Garfo', 'Kiwi', 'Faca']
frutas = []
talheres = []

for item in lista1 + lista2:
    if item in ['Maçã', 'Banana', 'Laranja', 'Pera', 'Kiwi']:
        frutas.append(item)
    else:
        talheres.append(item)

for fruta in frutas:
    if fruta in lista1:
        lista1.remove(fruta)
    if fruta in lista2:
        lista2.remove(fruta)

for talher in talheres:
    if talher in lista1:
        lista1.remove(talher)
    if talher in lista2:
        lista2.remove(talher)


print("Frutas:", frutas)
print("Talheres:", talheres)


idade_pessoa=int(input("digite sua idade: "))
if idade_pessoa<=10:
    print("você é uma criança")
elif idade_pessoa>= 11 and idade_pessoa <= 14:
    print("você é um pré adolescente")
elif idade_pessoa >= 15 and idade_pessoa <= 18:
    print ("você é um adolescente")
elif idade_pessoa>= 19 and idade_pessoa <= 40:
    print("você é um jovem adulto")
else:
    print("você é um idoso")
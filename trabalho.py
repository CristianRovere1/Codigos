nome=str(input("Digite seu nome:"))
idade=int(input("digite a sua idade:"))
nacionalidade=str(input("qual é sua nacionalidade"))
experiencia_em_anos = int(input("Digite a experiência em anos:"))

if idade >= 18 and experiencia_em_anos >= 2 and nacionalidade == "brasil":

    tela = (nome,idade,nacionalidade,experiencia_em_anos)
    print("você é elegível para o emprego.")
else:
    print("Você é inelegível para o emprego.")
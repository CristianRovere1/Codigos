lista_alunos = []
while True:
    nome_aluno = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
    
    
    if nome_aluno.lower() == 'fim':
        break
        
    lista_alunos.append(nome_aluno)

print("Lista de alunos:")
for aluno in lista_alunos:
    print(aluno)

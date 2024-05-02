investimento = float((input('Investimento Inicial:'))) 
tjurospercentagem = float((input('Taxa de Juros (em %) :')))
tjuro=tjurospercentagem/100
anos = int(input('Anos:'))
varfuturo= investimento*(1+tjuro*anos)
jurototal = investimento*tjuro*anos
juroano =investimento*tjuro
print('\n\n\t\t O valor futuro é de ',(varfuturo))
print(' Os juros totais é de ',(jurototal))
print( 'Os juros ao ano é de ',(juroano))

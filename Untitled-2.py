v = float(input('/ninsira o valor sem desconto do produto:'))

#obtendo a porcentagem do desconto

p = float(input('insira a porcentagem de desconto:'))

#calculando o valor descontado
vd = v * p/100

#calculando o valor com desconto
vf = v - vd

#imprimindo o resultado

print("n/==================================================/n")
print('o valor descontado é de:" R$ {:,.2f}'. format (vd))
print('the valor a pagar é de:" R$ {:,.2f}'. format (vf))
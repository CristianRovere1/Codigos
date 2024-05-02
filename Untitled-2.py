v = float(input('/ninsira o valor sem desconto do produto:'))

p = float(input('insira a porcentagem de desconto:'))

vd = v * p/100

vf = v - vd
print('o valor descontado é de:" R$ {:,.2f}'. format (vd))
print('the valor a pagar é de:" R$ {:,.2f}'. format (vf))

print('Bem-vindo a Maris Atacado!')
print('|----------------------------------------------|')
print('|   Quantidades	         |   Desconto         |')
print('|   Até 4	             |   0% na unidade    |')
print('|   Entre 5 e 19	         |   3% na unidade    |')
print('|   Maior ou igual a 100  |   10% na unidade   |')
print('|----------------------------------------------|')

x = float(input('Qual o valor unitário do produto?'))
y = int(input('Qual a quantidade desse produto?'))
z = x * y

if(y <= 4):
  total = z
elif(y >= 5 and y <= 19):
  total = z * 0.97
elif(y >= 20 and y <= 99):
  total = z * 0.94
elif(y >= 100):
  total = z * 0.9

print('O valor sem desconto é {} reais.' .format(z))
print('O valor com desconto é {} reais.' .format(total))
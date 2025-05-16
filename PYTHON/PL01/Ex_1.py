#1. Um banco concede um crédito especial aos seus clientes, variável com o saldo médio no último ano. Construa um
#algoritmo que leia o saldo médio de um cliente e calcule o valor máximo de crédito de acordo com a tabela abaixo.
#Mostre uma mensagem para informar o saldo médio e o valor do crédito.
#i. Abaixo de 200 – nenhum crédito
#ii. de 201 a 400 – até 20% do valor do saldo médio
#iii. de 401 a 600 – até 30% do valor do saldo médio
#iv. Acima de 600 – até 40% do valor do saldo médio



saldo = float(input("Saldo do último ano: " ))

if saldo <= 200:
    credito = 0
elif saldo >= 201 and saldo <= 400:
    credito = 0.2 * saldo
elif saldo >=401 and saldo <= 600:
    credito = 0.3 * saldo
else:
    credito = 0.4 * saldo

print(f"Saldo médio: {saldo} e crédito {credito}")

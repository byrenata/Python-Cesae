# 9. Ler uma sequência de pelo menos 5 números inteiros e em que a soma dos seus elementos seja superior a 100

sum = 0
num = 0
tot = 0
while tot < 5:
    num = int(input("Digite um número: "))
    tot += 1
    sum += num



print("Contador ",tot)
print("Soma ",sum)


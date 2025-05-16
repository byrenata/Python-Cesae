#8. Ler uma sequência de números inteiros até que sejam introduzidos 5 números ímpares e que mostre o maior número
#par. Se não tiver sido introduzido nenhum número par deve aparecer uma mensagem adequada.

totimp = 0
par = 0
maior = 0

while (totimp < 5):
    num = int(input("Digite um número: "))
    if num%2 == 1:
        totimp += 1
    elif num%2 == 0:
        par = num
        if par > maior:
            maior = par 
        
if par == 0:
    print("Não consta número par.") 
else:
    print(f"Maior número par: {maior}")
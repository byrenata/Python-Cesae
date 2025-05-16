#6. Ler números até ser inserido o número 0 (zero) e que permita calcular a soma e média de todos os números
#introduzidos.
tot = 0
sum = 0

while True:
    num = int(input("Informe um número ou digite 0: "))
       
    if num != 0:
        tot += 1
        sum += num        
    else:
        break
    if tot != 0:
        print(f"A soma dos números = {sum}, e a média = {sum/tot}")
    else:
       print("Nenhum número foi digitado.")    


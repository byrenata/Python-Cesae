#7. Determinar a percentagem dos N alunos de uma turma com idade superior a uma dada idade definida pelo utilizador.
#Se sabemos antecipadamente o total devemos usar CICLO FOR
padrao = int(input("Defina a idade: "))

tot = 0
maior = 0
perc = 0

while True:
    resp = input("Deseja informar idade [S/N]: ")
    if resp == 'S':
        idade = int(input("Informe sua idade: "))
        tot += 1
        if idade > padrao:
            maior +=1
            perc = (maior/tot) * 100

    if resp == 'N':
        break

print(f"Percentual de alunos com idade superior à idade padrão = {perc}%")


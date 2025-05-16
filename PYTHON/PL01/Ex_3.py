#3. Ler as notas de N alunos e calcular a média aritmética da turma.
#i. A média aritmética consiste em somar todos e dividir por o total de parcelas somadas.

totnotas = 0
sumnotas = 0

while True:
    resp = input("Deseja informar a nota? [S/N]")
    if resp == 'S':
        totnotas += 1
        nota = float(input("Informe a nota: "))
        sumnotas += nota
        med = sumnotas/totnotas
    else:
        resp == 'N'
        break
print(f"Média aritmética = {med}")

    

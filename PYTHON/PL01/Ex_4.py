#4. Ler as notas de N alunos de uma turma e apresentar o total de negativas e positivas encontradas.

totnotas = 0
totpositiva = 0
totnegativa = 0
somnotas = 0

while True:
    resp = input("Deseja informar notas? [S/N]")
    if resp == 'S':
        totnotas += 1
        nota = float(input("Informe a nota [De 0 a 20]: "))
        somnotas += nota
        media = somnotas/totnotas
        if nota > 10.0:
            totpositiva += 1
        else:
            totnegativa += 1
    else:
        break
print(f"Total de notas positivas: {totpositiva} e total de notas negativas: {totnegativa}")
#2. Uma empresa concede aumentos de salário aos seus funcionários, variáveis de acordo com o cargo. Construa um
#algoritmo que leia o salário e o cargo de um funcionário e calcule o novo salário. Se o cargo do funcionário não estiver
#na tabela, este deverá, então, receber 10% de aumento. Mostre o salário antigo, o novo salário e a diferença.
#i. Os cargos considerados (e seus códigos) são:
#ii. 101 Gerente 25%;
#iii. 102 Engenheiro 20%;
#iv. 103 Técnico 15%

cargo = input("Informe o cargo: ")
salario = float(input("Informe o salario: "))

if cargo == "gerente":
    aumento = 0.25
elif cargo == "engenheiro":
    aumento = 0.20
elif cargo == "tecnico":
    aumento = 0.15
else:
    aumento = 0.10

print(f'De acordo com seu cargo de {cargo} e salário = {salario} euros, o aumento será de {salario*aumento} euros. Novo salário = {salario + (salario*aumento)} euros.')
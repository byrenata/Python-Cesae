# Apresentar todos os números pares entre X e Y.

x = int(input("Digite x: "))
y = int(input("Digite y: "))

for i in range (x,y + 1):
    if(i%2==0):
        print (i)
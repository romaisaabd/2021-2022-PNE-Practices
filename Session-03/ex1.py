N = 11
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2,end=" ")
for i in range(2,N): #n es una constante
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
print()#esto lo hace para que no aparezca un espacio
#git app . --> hace que todos se metan en github
#gir add (nombre del file) --> lo mismo que lo de antes pero con un solo file
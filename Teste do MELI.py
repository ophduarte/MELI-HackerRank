print("Digite um número INTEIRO de 0 até 9")
maxDigit=input()
intmaxDigit=int(maxDigit)

numero=["0","0","0","0"]

numero[3]=intmaxDigit
numero[2]=intmaxDigit

soma=numero[3] + numero[2]

for x in range (0, intmaxDigit+1):
    if (soma+x<22):
        numero[1]=x
        rest=soma+x
    else:
        break

for z in range (0, intmaxDigit+1):
    if (rest+z<22):
        numero[0]=z
        soma=rest+z
    else:
        break

print("soma", soma)        
print(numero)

input()

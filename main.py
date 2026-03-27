from soma import somar
from subtracao import subtrair
from multiplicacao import multiplicar
from divisao import dividir 

print ("=== CALCULADORA ===")

print ("1 - soma")
print ("2 - subtração")
print ("3 - multiplicação")
print ("4 - divisão")

opcao = input ("Escolha uma opção (1/2/3/4):")

num1 = float (input("Digte o primeiro numero: "))
num2 = float (input("Digite o segundo numero: "))

if opcao == "1":
     resultado = somar (num1, num2)

elif opcao == "2":
    resultado = subtrair (num1, num2)

elif opcao == "3":
    resultado = multiplicar (num1, num2)

elif opcao == "4":
    resultado = dividir (num1, num2)

else:
    resultado = "opção invalida!"

print ("resultado:", resultado)
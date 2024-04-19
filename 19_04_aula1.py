#1 - Soma de dois números:
#Escreva um programa que solicite dois números ao usuário e imprima a soma deles.

x1 = int(input("Digite um número: "))
x2 = int(input("Digite outro número: "))
x = x1 + x2
print("A soma é ", x ,"")

#2 - Média de três números:
#Escreva um programa que solicite três números ao usuário e imprima a média deles.

x1 = int(input("Digite um número: "))
x2 = int(input("Digite um número: "))
x3 = int(input("Digite um número: "))
x = (x1 + x2 + x3) / 3

print("A média desses números é ", x)

#3 - Conversor de temperatura:
#Escreva um programa que converta uma temperatura em Celsius para Fahrenheit. 
#O usuário deve fornecer a temperatura em Celsius e o programa deve imprimir a temperatura equivalente em 
#Fahrenheit. A fórmula de conversão é: Fahrenheit = (Celsius * 9/5) + 32.

print("Bem vindo ao conversor de temperatura!")

x = float(input("Qual a temperatura, em celsius?"))
xf = x * 1.8 + 32

print("", x," em fahreinheit é ", xf,"")

#4 - Identificação de número par ou ímpar:
#Escreva um programa que solicite um número ao usuário e determine se ele é par ou ímpar. 

x = int(input("Digite um número: "))

if x % 2 == 0:
    print("O número é par")
else:
    printf("O número é impar")

#5 - Cálculo de fatorial:
#Escreva um programa que solicite um número inteiro positivo ao usuário e calcule o fatorial 
#desse número. O fatorial de um número inteiro positivo n é o produto de todos os inteiros positivos menores ou 
#iguais a n. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

x = int(input("Digite um número: "))

fatorial = 1
for i in range(1, x + 1):
    fatorial *= i
print("O fatorial de", x, "é", fatorial)

#6 - Verificador de ano bissexto:
#Escreva um programa que verifique se um ano fornecido pelo usuário é bissexto ou não. Um ano é bissexto se for 
#divisível por 4, exceto em anos que são divisíveis por 100 mas não são divisíveis por 400.

ano = int(input("Digite um ano: "))

if (ano % 4) == 0:
   if (ano % 100) == 0:
      if (ano % 400) == 0:
         print(ano, "é um ano bissexto")
      else:
         print(ano, "não é bissexto")
   else:
      print(ano, "é um ano bissexto")
else:
   print(ano, "não é bissexto")

#7- Verificação de número positivo ou negativo:
#Escreva um programa que solicite um número ao usuário e determine se ele é positivo, negativo ou zero.

num = int(input("Digite QUALQUER número: "))

if num == 0:
    print("Seu número é igual a 0")
elif num < 0:
    print("Seu número é negativo")
elif num > 0:
    print("Seu número é positivo")

#8- Comparação de dois números:
#Escreva um programa que solicite dois números ao usuário e determine qual é o maior deles. Se forem iguais, o programa deve informar isso.

n = int(input("Digite um número: "))
m = int(input("Digite outro número: "))

if n < m:
    print(m, "é o maior número")
elif n > m:
    print(n, "é o maior número")
elif n == m:
    print("Ambos os números são iguais")
          

#9- Verificação de idade:
#Escreva um programa que solicite a idade de uma pessoa e determine se ela é maior de idade
#(idade maior ou igual a 18 anos) ou menor de idade (idade menor que 18 anos).

idade = int(input("Qual é sua idade? "))

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

#10- Classificação de triângulos:
#Escreva um programa que solicite três comprimentos ao usuário, que representam os lados de um triângulo. O programa deve
#determinar se o triângulo é equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).

l1 = int(input("Lado 1 do triângulo: "))
l2 = int(input("Lado 2 do triângulo: "))
l3 = int(input("Lado 3 do triângulo: "))

if l1 == l2 == l3:
    print("Seu triângulo é equilátero.")
elif (l1 != l2 != l3):
    print("Seu triangulo é escaleno.")
elif (l1 == l2) or (l2 == l3) or (l3 == l1):
    print("Seu triângulo é isósceles.")

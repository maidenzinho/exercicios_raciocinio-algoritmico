# Exercício 1 (Informe se uma pessoa tem o mesmo nome que você)
'''
nome1 = input("Informe o nome da pessoa:")
nome2 = input("Digite seu nome:")

if nome1 == nome2 :
    print(f"Seu nome é igual ao nome da pessoa!")
else:
 print("Seu nome não é igual ao da pessoa!")
'''
# Exercício 2 (Informe se a pessoa digitou uma vogal ou consoante)
'''
letra = input("Digite uma letra:")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
  print(f"Você digitou uma vogal: {letra}")

else:
  print(f"Você digitou uma consoante: {letra}")
'''
# Exercício 3 (Informe o dia da semana a partir de um número entre 1 e 7. Exemplo, 1- Domingo, 2- Segunda etc. Se digitar outro valor deve aparecer “valor inválido”)
'''
dia = int(input("Digite um número de 1 a 7:"))

if dia == 1:
 print('Domingo')
elif dia == 2:
  print('Segunda')
elif dia == 3:
  print('Terça')
elif dia == 4:
 print('Quarta')
elif dia == 5:
  print('Quinta')
elif dia == 6:
  print('Sexta')
elif dia == 7:
 print('Sábado')
else:
  print('Valor inválido')
'''
# Exercício 4 (Informe o maior número entre dois números quaisquer)
'''
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

if(num1 > num2):
  print(f"O maior número é {num1}")
else:
  print(f"O maior número é {num2}")
'''
# Exercício 5 (Informe o maior número e o menor número entre dois números quaisquer)
'''
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

if (num1 > num2):
  print(f"O número {num1} é maior que {num2}")
else:
  print(f"O número {num2} é maior que {num1}")
'''
# Exercício 6 (Informe se um ano é bissexto ou não.)
'''
ano = int(input("Digite um ano qualquer : "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
'''
# Exercício 7 (Informe se um número é par (Use o módulo da divisão (%)))
'''
num = int(input("Digite um número:"))

if num % 2 == 0:
  print("O número é par!")
else:
  print("O número é impar!")
'''
# Exercício 8 (Informe se um número é múltiplo de um número N qualquer)
'''
num = int(input("Digite um número: "))
n = int(input("Digite o múltiplo de N: "))

if num % n == 0:
  print(f"{num} é múltiplo de {n}")

else:
  print(f"{num} não é múltiplo de {n}")
'''
# Exercício 9 (A partir de três notas de um aluno e informe se ele passou por média (70.0 ou mais))
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
if media >= 70.0:
  print(f'Aluno aprovado com média {media}')
else:
  print(f'Aluno reprovado com média {media}')
'''
# Exercício 10 (Verifique entre duas pessoas quem tem o maior nome e a mais velha.)
'''
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

if len(nome1) > len(nome2):
  print("A pessoa com o nome mais longo é", nome1)
elif len(nome2) > len(nome1):
  print("A pessoa com o nome mais longo é", nome2)
else:
  print("As pessoas têm nomes de comprimento igual.")

if idade1 > idade2:
  print("A pessoa mais velha é", nome1)
elif idade2 > idade1:
  print("A pessoa mais velha é", nome2)
else:
  print("As pessoas têm a mesma idade.")
'''
# Exercício 11 (Peça o login e senha de uma pessoa e informe se o login é valido.)
'''
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == "admin" and senha == "1234":
  print("Você está logado!")
else:
  print("Usuário ou senha incorretos")
'''
# Exercício 12 (Informe se uma pessoa tem idade para votar em 2023, a partir de seu ano de nascimento)
'''
ano = 2023
anonasc = int(input("Digite o ano do seu nascimento: "))

idade = ano - anonasc

if idade >= 18:
  print(f"Você já pode votar! Tem {idade} anos")
else:
  print(f"Você ainda não pode votar tem {idade} anos")
'''
# Exercício 13 (Informe se uma pessoa pode doar sangue (entre 18 e 59 anos))
'''
import datetime

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano = datetime.datetime.now().year
idade = ano - ano_nascimento

if idade >= 18 and idade <= 59:
  print("Você pode doar sangue!")
else:
  print("Você não pode doar sangue ainda!")
'''
# Exercício 14 (As maçãs custam 0,30 cada, se forem compradas menos do que uma dúzia, e 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra)
'''
compra = int(input("Quantas maçãs deseja comprar?: "))

if (compra <= 12):
  preco = compra * 0.30
  print(f"O total é de {preco}")

else:
  preco = compra * 0.25
  print(f"O total é de {preco}")
'''

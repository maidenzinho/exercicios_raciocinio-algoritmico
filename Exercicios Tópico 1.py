#Exercício 1 (SOMA)
'''
num = input('Digite um número:')
num1 = input('Digite outro número:')
num = int(num)
num1 = int(num1)

print(num + num1)
'''
#Exercício 2 (Antecessor, Número e Sucessor)
'''
num = input('Digite qualquer números:')
ant = int(num) - 1
suc = int(num) + 1

print(f'O número é {num}, seu antecessor é {ant} e seu sucessor é {suc}')
'''
#Exercício 3 (Troco)
'''
preco = input('Preço da compra:')
pago = input('Preço pago pelo comprador:')
troco = float(pago) - float(preco)

print('O troco é de:', troco)
'''
#Exercício 4 (Gorjeta)
'''
conta = input('Digite o valor da conta:')
gorjeta = float(conta) * 0.1

print('A gorjeta é de:', gorjeta)
'''
#Exercício 5 (Area m²)
'''
comprimento = 60.51
largura = 30.21

area = comprimento * largura

print(f"A area é de {area} m²")
'''
#Exercício 6 (Calcule a metragem quadrada de uma casa com 3 pavimentos)
'''
comprimento = 12.5
largura = 5.35
pavimentos = 3
area = comprimento * largura * pavimentos

print(f"A area é de {area} m²")
'''
#Exercício 7 (Calcule a média de idade de 5 pessoas)
'''
idade1 = 25
idade2 = 30
idade3 = 35
idade4 = 40
idade5 = 45

media = (idade1 + idade2 + idade3 + idade4 + idade5) / 5

print(f"A media de idade das pessoas é de {media} anos")
'''
#Exercício 8 (Calcule a idade a partir do ano de nascimento (Em anos))
'''
import datetime
anoatual = datetime.datetime.now().year
anodenasc = input("Digite seu ano de nascimento:")
anodenasc = int(anodenasc)
idade = anoatual - anodenasc

print(f"Você tem {idade} anos de vida")
'''
#Exercício 8 (Calcule a idade a partir do ano de nascimento (Em meses))
'''
import datetime

anoatual = datetime.datetime.now().year
anodenasc = input("Digite seu ano de nascimento:")
anodenasc = int(anodenasc)
idade = anoatual - anodenasc
mes = idade * 12
print(f"Você tem {mes} meses de vida")
'''
#Exercício 8 (Calcule a idade a partir do ano de nascimento (Em dias))
'''
import datetime

anoatual = datetime.datetime.now().year
anodenasc = input("Digite seu ano de nascimento:")
anodenasc = int(anodenasc)
idade = anoatual - anodenasc
dias = idade * 365
print(f"Você tem {dias} dias de vida")
'''
#Exercício 8 (Calcule a idade a partir do ano de nascimento (Todos juntos))
'''
import datetime

anoatual = datetime.datetime.now().year
anodenasc = input("Digite seu ano de nascimento:")
anodenasc = int(anodenasc)
idade = anoatual - anodenasc
meses = idade * 12
dias = idade * 365
print(f"Você tem {idade} anos, {meses} meses e {dias} dias de vida")
'''
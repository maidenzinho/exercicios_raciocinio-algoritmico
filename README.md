# Exercícios de python da aula de Raciocinio Algoritmico, Cibersegurança PUCPR

### Todos estão comentados, apenas remova as 3 aspas em cima e embaixo de cada exercício!

# Exemplo (Soma)

```
num = input('Digite um número:')
num1 = input('Digite outro número:')
num = int(num)
num1 = int(num1)

print(num + num1)
```
# Tópico 01 - Introdução   

# Tópico 02 - Estruturas de seleção (IF)

### Exemplo:
### Informe se uma pessoa tem o mesmo nome que você
```
nome_pessoa = input("Informe o nome da pessoa: ")
seu_nome = input("Informe seu nome: ")

if nome_pessoa == seu_nome:
    print("A pessoa tem o mesmo nome que você")
else:
    print("A pessoa não tem o mesmo nome que você")
``` 

# Tópico 03 - Estruturas de seleção múltiplas (ELIF)

### Exemplo:
### Implemente um seletor de canais para informar que canal a pessoa está assistindo, sendo:
```
print(
    "Canais disponiveis: [2]Band [4]SBT [6]CNT [7]Record [9]Cultura [12]Globo")
select = int(input("Selecione um canal: "))

if (select == 2):
  print("Você está assistindo [2]Band")
elif (select == 4):
  print("Você está assistindo [4]SBT")
elif (select == 6):
  print("Você está assistindo [6]CNT")
elif (select == 7):
  print("Você está assistindo [7]Record")
elif (select == 9):
  print("Você está assistindo [9]Cultura")
elif (select == 12):
  print("Você está assistindo [12]Globo")
else:
  print("Canal não encontrado")
```

# Tópico 04 - Estruturas de repetição (While)

# Tópico 05 - Estruturas de repetição (FOR)

# Tópico 06 - Arrays - Vetores

# Tópico 07 - Arrays - Matrizes

# Tópico 08 - Funções

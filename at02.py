# Prática sobre o uso de estruturas condicinais como if, else, e elif
# 1.  Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

if num_1 > num_2:
    print(f'O primeiro número é maior: {num_1}')
elif num_2 > num_1:
    print(f'O segundo número é maior: {num_2}')
else: 
    print('Os dois números são iguais.')

# 2. Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

variacao  = float(input('Digite o percentual de crescimento de produção da sua empresa: '))

if variacao > 0:
    print(f'Houve um crescimento de {variacao}%')
elif variacao < 0:
    print(f'Houve um decrescimento de {variacao}%')
else:
    print('Não houve crescimento ou decrescimento')

# 3. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = str(input('Digite uma letra do alfabeto: ').lower())
vogais = 'aeiou'

if letra in vogais:
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')

# 4. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

ano_1 = float(input('Informe o valor do carro no primeiro ano: '))
ano_2 = float(input('Informe o valor do carro no segundo ano: '))
ano_3 = float(input('Informe o valor do carro no terceiro ano: '))

maior_valor = ano_1
if ano_2 > maior_valor:
    maior_valor = ano_2
if ano_3 > maior_valor:
    maior_valor = ano_3

menor_valor = ano_1
if ano_2 < menor_valor:
    menor_valor = ano_2
if ano_3 < menor_valor:
    menor_valor = ano_3

print(f'O maior valor foi de R${maior_valor}')
print(f'O menor valor foi de R${menor_valor}')

# 5. Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

produto_1 = float(input('Informe o valor do primeiro produto: '))
produto_2 = float(input('Informe o valor do segundo produto: '))
produto_3 = float(input('Informe o valor do terceiro produto: '))

mais_barato = produto_1
if produto_2 < mais_barato:
    mais_barato = produto_2
if produto_3 < mais_barato:
    mais_barato = produto_3

print(f'O produto mais barato custa R${mais_barato}')

# 6. Escreva um programa que leia três números e os exiba em ordem decrescente.

num_1 = int(input('Informe o primeiro número: '))
num_2 = int(input('Informe o segundo número: '))
num_3 = int(input('Informe o terceiro número: '))

maior_num = num_1
if num_2 > maior_num:
    maior_num = num_2
if num_3 > maior_num:
    maior_num = num_3

menor_num = num_1
if num_2 < menor_num:
    menor_num = num_2
if num_3 < menor_num:
    menor_num = num_3

if (num_1 != maior_num) and (num_1 != menor_num):
    meio_num = num_1
elif (num_2 != maior_num) and (num_2 != menor_num):
    meio_num = num_2
else:
    meio_num = num_3

print(maior_num, meio_num, menor_num)

# 7. Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = str(input('Em qual turno você estuda?: '))

if turno == 'manhã':
    print('Bom dia!')
elif turno == 'tarde':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
else:
    print('Valor inválido!')

# 8. Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')

# 9. Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

num = float(input('Digite um número: '))

if num % 1 == 0:
    print(f'O número {num} é inteiro')
else:
    print(f'O número {num} é decimal')

# 10. Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))
operacao = input('Informe a opração desejada: ')

if operacao == '+':
    resultado = num_1 + num_2
elif operacao == '-':
    resultado = num_1 - num_2
elif operacao == '*':
    resultado = num_1 * num_2
elif operacao == '/':
    resultado = num_1 / num_2
else:
    print('Operação inválida')
    resultado = 0

if resultado % 1 == 0:
    print('O resultado é inteiro.')
else:
    print('O resultado é decimal')

if resultado % 2 == 0:
    print('O resultado é par')
else:
    print('O resultado é ímpar.')

if resultado > 0:
    print('O resultado é positivo')
elif resultado == 0:
    print('O resultado é neutro')
else:
    print('O resultado é negativo')

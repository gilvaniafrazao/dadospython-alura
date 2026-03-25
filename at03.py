# prática do uso de estruturas de repetição como o while e o for
# 1. Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite o segundo número: '))

if num_1 < num_2:
    for i in range(num_1 + 1, num_2):
        print(i)
elif num_1 > num_2:
    for i in range(num_2 + 1, num_1):
        print(i)
else:
    print('Os número são iguais')

# 2. Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

colonia_a = 5
colonia_b = 10

taxa_a = 0.03
taxa_b = 0.015

dias = 0

while colonia_a <= colonia_b:
  colonia_a *= 1 + taxa_a
  colonia_b *= 1 + taxa_b
  dias += 1

print(f'Irá levar {dias} dias para a colônia A ultrapassar a colônia B.')

# 3. Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for i in range(15):
  nota = float(input('Digite uma nota entre 0 e 5: '))

  while nota < 0 or nota > 5:
    nota = float(input('Valor inválido! Digite uma nota entre 0 e 5: '))

# 4. Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

temperatura = float(input('Insira a temperatura em Celsius: '))

contadora = 0
soma = 0

while temperatura != -273:
    soma += temperatura
    contadora += 1
    temperatura = float(input('Insira a temperatura em Celsius: '))

media = soma / contadora

print(f'A média das temperaturas é: {media}')

# 5. Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

num = int(input('Informe um número inteiro: '))

fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print('Fatorial: ', fatorial)

# 6. Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

num = int(input('Informe um número inteiro: '))

print(f'Tabuada do {num}:')

for i in range(1,11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

# 7. Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Informe um número inteiro: '))

primo = True

if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')

# 8. Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

idade = int(input('Informe a idade: '))

contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0

while idade >= 0:
    if idade >= 0 and idade <= 25:
        contador_0_25 += 1
    elif idade >= 26 and idade <= 50:
        contador_26_50 += 1
    elif idade >= 51 and idade <= 75:
        contador_51_75 += 1
    elif idade >= 76 and idade <= 100:
        contador_76_100 += 1
    
    idade = int(input('Informe a idade: '))

print('Distribuição de idades:')
print('[0-25]: ', contador_0_25)
print('[26-50]: ', contador_26_50)
print('[51-75]: ', contador_51_75)
print('[76-100]: ', contador_76_100)

# 9. Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira: Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4). Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).

votos_cand1 = 0
votos_cand2 = 0
votos_cand3 = 0
votos_cand4 = 0
votos_nulos = 0
votos_brancos = 0

voto = int(input('Informe o número da sua votação: '))

for i in range(20):
    if voto == 1:
        votos_cand1 += 1
    elif voto == 2:
        votos_cand2 += 1
    elif voto == 3:
        votos_cand3 += 1
    elif voto == 4:
        votos_cand4 += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    
    voto = int(input('Informe o número da sua votação: '))
    
print('Votos contabilizados:')
print('Candidato 1: ', votos_cand1)
print('Candidato 2: ', votos_cand2)
print('Candidato 3: ', votos_cand3)
print('Candidato 4: ', votos_cand4)
print('Votos nulos: ', votos_nulos)
print('Votos brancos: ', votos_brancos)
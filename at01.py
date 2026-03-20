# Coleta e amostragem de dados
# 1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima "Olá, [nome]!".

nome = input("Escreva o seu nome: ")
print(f"Olá, {nome}!")

# 2. Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima "Olá, [nome], você tem [idade] anos."

nome = input("Escreva o seu nome: ")
idade = int(input("Escreva a sua idade: "))
print("Olá, %s, você tem %d anos." %(nome, idade))

# 3. Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima "Olá, [nome], você tem [idade] anos e mede [altura] centímetros!"

nome = input("Escreva o seu nome: ")
idade = int(input("Escreva a sua idade: "))
altura = float(input("Escreva a sua altura: "))
print("Olá, %s, você tem %d anos e mede %.2f centímetros!" %(nome, idade, altura))

# Calculadora com operadores
# 1. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

num_1 = int(input("Insira o primeiro número: "))
num_2 = int(input("Insira o segundo número: "))
soma = num_1 + num_2
print(soma)

# 2. Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.

num_1 = int(input("Insira o primeiro número: "))
num_2 = int(input("Insira o segundo número: "))
num_3 = int(input("Insira o terceiro número: "))
soma = num_1 + num_2 + num_3
print("A soma é: %d" %(num_1 + num_2 + num_3))

# 3. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

num_1 = int(input("Insira o primeiro número: "))
num_2 = int(input("Insira o segundo número: "))
print("A subtração é: %d" %(num_1 - num_2))

# 4. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.

num_1 = int(input("Insira o primeiro número: "))
num_2 = int(input("Insira o segundo número: "))
print("A multiplicação é: %d" %(num_1 * num_2))

# 5. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numerador = float(input("Insira o numerador: "))
denominador = float(input("Insira o denominador: "))
print("A divisão é: %.2f" %(numerador / denominador))

# 6. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

operador  = int(input("Insira o operador: "))
potência = int(input("Insira a potência: "))
print("A exponenciação é: %d" %(operador ** potência))

# 7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0. 

numerador = float(input("Insira o numerador: "))
denominador = float(input("Insira o denominador: "))
print("A divisão inteira é: %.2f" %(numerador // denominador))

# 8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numerador = float(input("Insira o numerador: "))
denominador = float(input("Insira o denominador: "))
print("O resto da divisão é: %.2f" %(numerador % denominador))

# 9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

nota_1 = float(input("Insira a primeira nota do aluno: "))
nota_2 = float(input("Insira a segunda nota do aluno: "))
nota_3 = float(input("Insira a terceira nota do aluno: "))
print("A média do aluno é: %.2f" %((nota_1 + nota_2 + nota_3) / 3))

#Editando textos
# 1. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.

frase = "Deus é bom em todo tempo!"
print(frase)

# 2. Crie um código que solicite uma frase e depois imprima a frase na tela.

frase = input("Insira aqui o seu versículo favorito: ")
print(frase)

# 3. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.

frase = input("Insira uma frase aqui: ")
print(frase.upper())

# 4. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.

frase = input("Insira uma frase aqui: ")
print(frase.lower())

# 5. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

frase = " As estações mudaram! "
print(frase.strip())

# 6. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.

frase = input("Digite a sua música favorita: ")
print(frase.strip())

# 7. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.

frase = input("Digite o nome do seu filme favorito: ")
print(frase.strip().lower())

# 8. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.

frase = input("Diga o nome do seu personagem favorito: ")
print(frase.replace('e','f'))

# 9. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.

frase = input("Informe o local de destino: ")
print(frase.lower().replace('a',chr(64)))

# 10. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.

frase = input("Qual disciplina deseja estudar?: ")
print(frase.lower().replace('s',chr(36)))
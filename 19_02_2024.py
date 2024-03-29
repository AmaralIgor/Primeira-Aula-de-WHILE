# -*- coding: utf-8 -*-
"""19/02/2024.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10L8GuD5YtITL7L3vVpqv_nRYbnBRzdvQ

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
"""

while True:
  nota = int(input("Digite uma nota de 0 a 10: "))
  if nota >= 0 and nota <= 10:
    break
  print("Valor inválido")

"""Faça um programa que calcule o mostre a média aritmética de N notas."""

quantidade = int(input("Digite a quantidade de notas: "))
contador = 0
soma = 0
media = 0

while contador < quantidade:
  soma += float(input("Digite a nota do Aluno(a): "))
  contador += 1
media = soma / quantidade
print(f"A sua média é {media}")

"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a
pedir as informações
"""

while True:
  nome_user = input("Digite um nome de usuário: ")
  senha_user = input("Digite sua senha: ")
  if nome_user != senha_user:
    break
  print("Erro")

"""Um funcionário de uma empresa recebe aumento salarial anualmente.
Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$
1.000,00; Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de
1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
percentual do ano anterior. Faça um programa que determine o salário atual desse
funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o
salário inicial do funcionário.
"""

salario = float(input("Digite o Valor do Sálario"))
percentual = 1.5
ano = 1996

while ano < 2024:
  reajuste = salario * percentual / 100
  salario_reajustado = salario + reajuste
  print(ano, salario_reajustado, reajuste, percentual)
  percentual *= 2
  ano += 1

"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
  nome = input("Digite seu nome com no mínimo 3 caracteres: ")
  if len(nome) < 3:
    print("Nome Inválido.")
    continue

  idade = int(input("Digite sua idade: "))
  if idade < 0 or idade > 150:
    print("Idade Inválida.")
    continue

  salario = float(input("Digite seu sálario: "))
  if salario < 0:
    print("Salário Inválido.")
    continue

  sexo = str(input("Digite seu sexo com F para feminino, M para masculino: ")).upper()
  if sexo != "M" and sexo != "F":
    print("Sexo Inválido.")
    continue

  estado_civil = input("Digite seu Estado Civil com S para solteiro(a), C para casado(a), V para viúvo(a) e D para divorciádo(a): ")
  if estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D":
    print("Estado Civil Inválido.")
    continue
  break

"""Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pais_a = 80000
pais_b = 200000
ano = 0

crescimento_a = 3.0 / 100
crescimento_b = 1.5 / 100

while pais_a <= pais_b:
  ano += 1
  pais_a += pais_a * crescimento_a
  pais_b += pais_b * crescimento_b

print(f"Irá levar {ano} anos para o país A se igualar ao país B.")

"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120
"""

fatorial = int(input("Digite um número inteiro: "))
contador = 0
resultado = 1

while fatorial > contador:
  resultado += resultado * contador
  contador += 1
  print(resultado)
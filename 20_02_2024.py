# -*- coding: utf-8 -*-
"""20/02/2024.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kbuy417bwufDnx72TuzYOwWqRIop6e6I

Faça um programa que solicite ao usuário números indefinidamente até que ele
digite 0. Em seguida, o programa deve imprimir a média dos números digitados
"""

numero = float(input("Digite um número qualquer ou digite 0 para parar:"))
soma = 0
contagem = 0

while numero != 0:
  soma += numero
  contagem += 1
  numero = float(input("Digite um número qualquer ou digite 0 para parar:"))

media = soma / contagem if contagem != 0 else 0
print(f"A média dos números digitados são: {media}")

"""A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um
programa capaz de gerar a série até o n−ésimo termo.
"""

valor1 = 1
valor2 = 1
contador = 0
quantidade = 10
print(valor1)
print(valor2)

while contador < quantidade:
  soma = valor1 + valor2
  valor1 = valor2
  valor2 = soma
  print(soma)
  contador += 1
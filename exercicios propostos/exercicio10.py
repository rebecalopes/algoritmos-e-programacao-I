produto1 = input("Digite o nome do primeiro produto ")
quant1 = int(input("Digite a quantidade vendida "))
valor1 = float(input("Digite o valor unitario "))
produto2 = input("Digite o nome do segundo produto ")
quant2 = int(input("Digite a quantidade vendida "))
valor2 = float(input("Digite o valor unitario "))
produto3 = input("Digite o nome do terceiro produto ")
quant3 = int(input("Digite a quantidade vendida "))
valor3 = float(input("Digite o valor unitario "))

total1 = (quant1 * valor1)
total2 = (quant2 * valor2)
total3 = (quant3 * valor3)

somaTotal = total1 + total2 + total3

print("O valor da venda de {0} foi {1:.2fa}".format(produto1,total1))
print("O valor da venda de {0} foi {1:.2fa}".format(produto2,total2))
print("O valor da venda de {0} foi {1:.2fa}".format(produto3,total3))
print("O valor total das vendas foi de {0:.2f}".format(somaTotal))


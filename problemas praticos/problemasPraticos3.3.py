ano = eval(input("Qual o ano? "))

if ano % 4 == 0:
    print("pode ser um ano bissexto")
else:
    print("definitivamente nao e um ano bissexto")

bilhete = [12,47,38,90,4]
loteria = [12,74,38,90,2]

if bilhete == loteria:
    print('Voce ganhou')
else:
    print('Mais sorte da proxima vez')
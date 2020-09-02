idade = eval(input('Digite sua idade '))

if idade > 62:
    print('Voce pode obter beneficios de pensao')

nome = str(input('Qual o seu nome? '))

jogadores = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']

if nome in jogadores:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')

golpes = eval(input('Quantidade de golpes '))
defesa = eval(input('Numero de defesa '))

if golpes > 10 and defesa == 0:
    print('Voce esta morto')

from math import sqrt

x1= float(input('Digite a primeira coordenada do eixo x '))
y1 = float(input('Digite a primeira coordenada do eixo y '))
x2 = float(input('Digite a segunda coordenada do eixo x '))
y2 = float(input('Digite a segunda coordenada do eixo y '))

d = sqrt((x1 - x2) ** 2  + (y1 - y2) ** 2)
print('A distancia entre os pontos e {0:.3f}'.format(d))
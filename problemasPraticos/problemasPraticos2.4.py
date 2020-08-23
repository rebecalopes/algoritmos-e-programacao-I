#Comece executando as instruçoes de atribuiçao

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

#Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para
#'ant bat cod'
expre1 = s1 + ' ' + s2 + ' ' + s3
print (expre1)

#'ant ant ant ant ant ant ant ant ant ant'
expre2 = (s1 + ' ') * 10
print(expre2)

#'ant bat bat cod cod cod'
expre3 = s1 + ' ' + (s2 + ' ' * 2) + (s3 + ' ' * 3)
print(expre3)

#'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
expre4 = (s1 + ' ' + s2 + ' ') * 7 
print(expre4)

#'batbatcod batbatcod batbatcod batbatcod batbatcod'
expre5 = (s1+s2+s3+' ') * 5
print(expre5)

#ordem que os operadores nas expressoes a seguir sao avaliados

#2 + 3 == 4 or a >= 5
((2 + 3) == 4) or (a >= 5)

#lst[1] * -3 < -10 == 0
(((lst[1]) * (-3)) < (-10)) == 0

#(lst[1] * -3 < -10) in [0, True]
(((lst[1]) * (-3)) < (-10)) in [0, True]

#2 * 3**2
2 * (3**2)

#4 / 2 in [1, 2, 3]
(4 / 2) in [1, 2, 3]
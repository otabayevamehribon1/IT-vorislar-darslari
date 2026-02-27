# def yigindi(a,b):
#     natija= a+b 
#     print(f"yigindi {natija}")
# yigindi(23,56)

# def ayirma (a,b):
#     natija=a-b
#     print(f"ayirma {natija}")
# ayirma(23,43)

# def kopaytma(a,b):
#     natija= a*b 
#     print(f"kopaytma {natija}")
# kopaytma(34,43)

# def bolish(a,b):
#     """Iki sonni bolish 0 ga bolishni tekshirish funksiyasi"""

#     if b == 0:
#         print("Nolga bo'lish mumkin emas!")
#     else:
#         natija = a / b
#         print(f"bolish {natija}")
# bolish(0,0)

# def sonlar(son):
#     """juft bolsa true, toq bolsa false """
#     if son % 2 == 0:
#         print("true")
#     else:
#         print("false")
# sonlar(28)

# def sonlar(son):
#     """ musbat yoki manfiylikini aniqlash"""
#     if son > 0:
#         print("musbat")
#     elif son < 0:
#         print("manfiy")
#     else:
#         print("nol")
# sonlar(0)

# def sonning_kvadrat(a):
#    return a**2
# print(sonning_kvadrat(5))

# def sonning_kubi(a):
#     return a**3
# print(sonning_kubi(7))

# def orta_arifmetik(a,b,c):
#     """a,b,csonlarining orta arifmetigini hisoblovchi funksiya"""
#     yigindi= a+b+c
#     daraja=3 
#     orta_arifmetik=yigindi/daraja
#     natija= f"{a}, {b}, {c}, sonlarining orta arifmetigi {orta_arifmetik} ga teng"
#     return natija
# print(orta_arifmetik(2,4,8,))


# def max_of_two(a,b):
#     """a va b sonlarining kattasini aniqlovchi funksiya"""
#     if a > b:
#         print(f"{a} soni {b} sonidan katta")
#     elif a < b:
#         print(f"{b} soni {a} sonidan katta")
#     else:
#         print("Ikkala son teng")
# max_of_two(23,56)
# max_of_two(67,67)
# max_of_two(34,56)

# def max_of_three(a,b,c):
#     return min(a,b)
# print(max_of_three(24,55))


# def baholash( ball):
#     if 10<= ball < 30:
#         print("qoniqarsiz")
#     elif 30<= ball <60:
#         print("qoniqarli")
#     elif 60 <= ball <80:
#         print("yaxshi")
#     elif 80<= ball <100:
#         print("a'loo !")
# baholash(45)
# baholash(80)


def solishtirish(a,b,c):
 if a>b and a>c :
  print(a)
 elif b>a and b>c :
  print(b)
 elif c>a and c>b:
   print(c)
solishtirish(34,6,47)



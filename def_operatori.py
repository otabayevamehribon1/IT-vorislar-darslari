# def kopaytma (a,b,c,d):
#     """a,b,c,d qiymatlarni kopaytma korinishda chiqaruvchi funksiya"""
#     kopaytma=a*b*c*d
#     return kopaytma
# print(kopaytma(3,4,5,6))
   

# def darajaga_oshirish(a,b):
#     """a sonini b darajaga oshirish"""
#     daraja=a**b
#     return daraja
# print(darajaga_oshirish(92,2))

# def maxsimum(a,b):
#     """a va b sonlaridan kattasini qaytaruvchi funksiya"""
#     if a>b:
#         return a
#     else:
#         return b
# print(maxsimum(3,4))


# def ishorani_aniqlovchi(a):
#     """a sonining ishorasini aniqlovchi funksiya"""
#     if a>0:
#         return "musbat"
#     elif a<0:
#         return "manfiy"
#     else:
#         return "nol"
# print(ishorani_aniqlovchi(-3))

# def oliy_talimga_kirish(ozingizni_balingiz):
#  """OLiy talimga kirishni aniqlash(sirtqi,kantrakt,grant)"""
# print("TaTu oliy talimga kirish uchun kerakli ball 189")
# if ozingizni_balingiz >= 155:
#     print("Siz oliy talimga qabul qilindingiz")
# elif  ozingizni_balingiz >80 and ozingizni_balingiz<150:
#    print("Tabriklaymiz! Siz kantrakt asosida oqishga qabul qilindingiz")
# elif ozingizni_balingiz >85 and ozingizni_balingiz<155:
#     print("Tabriklaymiz! Siz sirtqi asosida oqishga qabul qilindingiz")
# elif ozingizni_balingiz <80:
#     print("Afsuski siz oliy talimga qabul qilinmadingiz")
# oliy_talimga_kirish(90)
# oliy_talimga_kirish(160)
# oliy_talimga_kirish(54)



# def yoshni_aniqlash(t_yil) :
#     """yoshni aniqlash funksiyasi"""
#     ism= input("Ismingiz kim ? :")
#     familiya= input("familiyangizni kiriting :") 
#     natija= 2026-t_yil
#     return f"Hurmatli {familiya.title()} {ism.title()}, hozirda siz {natija} yoshda ekansiz. Kelajak ishlaringizga omad !"
# print(yoshni_aniqlash(2011))


# def qoshish_ayirish_bolish_kopaytirish(a,b,c):
#     """a va b sonlarini c amaliga kora bajaruvchi funksiya"""
#     if c=="+":
#         return f"{a} + {b} = {a+b}"
#     elif c=="-":
#         return f"{a} - {b} = {a-b}"
#     elif c=="*":
#         return f"{a} * {b} = {a*b}"
#     elif c=="/":
#         return f" {a} / {b} = {a/b} "
# print(qoshish_ayirish_bolish_kopaytirish(123,454,"+"))
# print(qoshish_ayirish_bolish_kopaytirish(908,435,"-"))
# print(qoshish_ayirish_bolish_kopaytirish (3432,2,"*") )
# print(qoshish_ayirish_bolish_kopaytirish(18,2,"/"))

# def orta_geometrik(a,b,c,d,e):

# kopaytma =  a*b*c*d*e
# daraja= (1/5)
# orta_geometrik=kopaytma**daraja
# natija= f"{a}, {b}, {c}, {d} va {e} sonlarining orta geometrigi {orta_geometrik} ga teng"
# return natija
# print(orta_geometrik(2,4,8,16,32))

# def orta_arifmetik(a,b,c,d,e):
#     """a,b,c,d,e sonlarining orta arifmetigini hisoblovchi funksiya"""
#     yigindi= a+b+c+d+e
#     daraja=5
#     orta_arifmetik=yigindi/daraja
#     natija= f"{a}, {b}, {c}, {d} va {e} sonlarining orta arifmetigi {orta_arifmetik} ga teng"
#     return natija
# print(orta_arifmetik(2,4,8,16,32))

# maxsulotlar=["olma","xoddog","pecheniya","cola","ruchka","daftar"]
# print(f"Bufetga hush kelibsiz! Bizda {maxsulotlar} bor. Sizga nima kerak ?")

# def savdogarlik(maxsulot):
#     if maxsulot == 'olma' :
#         print(f"Bizdda {maxsulot} 10 ming som . Olasizmi ?")
#     elif maxsulot == 'xoddog' :
#         print(f"Bizdda {maxsulot} 7 ming som . Olasizmi ?")
#     elif maxsulot == 'pecheniya' :
#         print(f"Bizdda {maxsulot} 5 ming som . Olasizmi ?")
#     elif maxsulot == 'cola' :
#         print(f"Bizdda {maxsulot} 7 ming som . Olasizmi ?")
#     elif maxsulot == 'ruchka' :
#         print(f"Bizdda {maxsulot} 2 ming som . Olasizmi ?")
#     elif maxsulot == 'daftar' :
#         print(f"Bizdda {maxsulot} 1 ming som . Olasizmi ?")
# savdogarlik("olma")
# savdogarlik("xoddog")
# savdogarlik("cola")

def yigindi(a,b,c,d,):
    natija= a+b+c+d
    print(f"yigindi {natija}")
yigindi(23,56,67,7,)
    
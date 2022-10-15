#Değişkenler olmadan 2 öğrencinin sınav notunu hesaplayalım.
# print( (80*0.40) + (75*0.60)  )
 # print( (45*0.40) + (60*0.60)  )
 #değişkenlerle 2 öğrencinin sınav notlarını hesaplayalım.
sinav1_yuzde = 0.4
sinav2_yuzde = 0.6

print(   (80*sinav1_yuzde) + (75*sinav2_yuzde)   )
print(   (45*sinav1_yuzde) + (60*sinav2_yuzde)   )

# DEĞİŞKEN TANIMLAMA KURALLARI


# Rakam ile başlayamaz
# 1sayi = 85 hata verdi
sayi1 = 85
print (sayi1)

#Büyük küçük harfe duyarlıdır
number = 12
NUMBER = 15
print (number)
print (NUMBER)

#Türkçe karakterler kullanılmaz
# yaş  = 18 hata verdi

yas = 18

age = 17

print(yas)
print(age)

x = 1 #integer

y = 1.2 # float

ad = "Asim" #string

sinav_basarili_mi = True #boolean

print(x+y)

#print(x+ad) #hata verdi

print(x+sinav_basarili_mi)
# print(ad+sinav_basarili_mi) # hata verdi


print(sinav_basarili_mi)

print(str(sinav_basarili_mi))

print(int(sinav_basarili_mi))

print(type(str(x)))
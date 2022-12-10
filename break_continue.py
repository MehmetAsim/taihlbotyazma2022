"""
break: döngüyü sonlandırır
Continue: döngünün ilgili turunu sonlandırır

"""



#0'dan 10'a kadar olan sayıları 5 hariç ekrana yazdıralım

#for sayi in range(10):
 #   if sayi == 5:
#
#    print(sayi):
#



for sayi in range(1,100):
    if sayi % 2 == 0:
        continue
    print(sayi)
#Öğrencinin adını soy adını ve notlarını alıp ekrana yazdıralım
ad = input("Öğrenci Adı:")

soyad =input("Öğrenci Soyadı:")

notlar = input("Sınav notları (virgülle ayrılmış):")



def ogrenci_kaydet(ad, soyad, notlar):
    notlar_list = notlar.split(",")

    notlar_list = [int(x) for x in notlar.split(",")]

    ortalama = sum(notlar_list) / len(notlar_list)

    dosya = open("öğrenciler.txt", mode="a", encoding="utf-8")

    dosya.write(f"Ad: {ad}, Soyad: {soyad}, Notlar: {notlar}, Ortalama: {ortalama} ")

    dosya.close()

    ogrenci_kaydet(ad, soyad , notlar"")
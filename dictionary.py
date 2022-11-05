"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "Mehmet Asım"
    "soyad": "KUŞ"
"""
isimler = ("Ahmet" , "Mehmet")
numaralar = [66 , 75]

numara  = int(input("Öğrenci Numarasını Yazınız: "))

#print(numaralar.index(numara))

ogrenciler = {66:"Ahmet" ,75:"Mehmet" }
print(ogrenciler[numara])

kisiler = {

    1: {
        "ad": "Mehmet",
        "soyad":"Kuş",
        "cinsiyet": True,
        "dersler": ["Matematik" , "Fizik" , "Kimya"]
       },
    45: {
        "ad":"Zeynep",
        "soyad":"Kuş",
        "cinsiyet": False,
        "dersler": ["Matematik" , "Fen Bilimleri" , "Beden Eğitimi"]

          }
}

print(kisiler[45]["dersler"])


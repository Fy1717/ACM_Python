# Yaşınızı yıl, ay, gün olarak hesaplayan bir fonksiyon

from datetime import datetime

def yas_hesapla(isim, dogum_yili, dogum_ayi, dogum_gunu):
    simdi = datetime.now()  # Mevcut tarih ve saat
    
    dogum_tarihi = datetime(dogum_yili, dogum_ayi, dogum_gunu)  # Doğum tarihi
    fark = simdi - dogum_tarihi  # Farkı hesaplar

    # Yıl, ay ve gün olarak yaş hesaplama
    yil = fark.days // 365
    kalan_gunler = fark.days % 365
    ay = kalan_gunler // 30
    gun = kalan_gunler % 30

    return f"{isim} {yil} yıl {ay} ay {gun} gün yaşındadır."

try:
    name = input("ismnizi girin : ")  # "furkan"
    year = int(input("doğum tarihinizin yılını giriniz : "))  # "1997"
    month = int(input("doğum tarihinizin ayını giriniz : "))  # "1"
    day = int(input("doğum tarihinizin gününü giriniz : "))  # "17"
    
    print(yas_hesapla(name, year, month, day))
except Exception as e:
    print("hata : ", str(e))    

# Örnek kullanım


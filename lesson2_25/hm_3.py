# Yaşınızı yıl, ay, gün olarak hesaplayan bir fonksiyon

from datetime import datetime

def yas_hesapla(isim, dogum_yili, dogum_ayi, dogum_gunu):
    """
    İsme ve doğum tarihine göre kişinin yaşını hesaplar.
    Args:
    isim (str): Kişinin adı.
    dogum_yili (int): Doğum yılı.
    dogum_ayi (int): Doğum ayı.
    dogum_gunu (int): Doğum günü.
    Returns:
    str: Kişinin yaşını "isim X yıl Y ay Z gün yaşındadır" formatında döndürür.
    """
    simdi = datetime.now()  # Mevcut tarih ve saat
    dogum_tarihi = datetime(dogum_yili, dogum_ayi, dogum_gunu)  # Doğum tarihi
    fark = simdi - dogum_tarihi  # Farkı hesaplar

    # Yıl, ay ve gün olarak yaş hesaplama
    yil = fark.days // 365
    kalan_gunler = fark.days % 365
    ay = kalan_gunler // 30
    gun = kalan_gunler % 30

    return f"{isim} {yil} yıl {ay} ay {gun} gün yaşındadır."

# Örnek kullanım
print(yas_hesapla("Resul", 2000, 4, 25))

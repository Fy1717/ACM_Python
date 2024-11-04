# Dersi geçen öğrencilerin listesini ve sınıf ortalamasını veren bir fonksiyon

def dersi_gecenler(ogrenci_notlari, gecme_notu):
    """
    Öğrenci notları ve geçme notuna göre dersi geçen öğrencilerin listesini ve sınıf ortalamasını verir.
    Args:
    ogrenci_notlari (dict): Öğrenci adı ve notları içeren sözlük.
    gecme_notu (int): Ders için belirlenen geçme notu.
    """
    gecenler = []  # Geçen öğrencilerin listesi
    toplam_not = 0  # Notların toplamı

    # Öğrenci notları üzerinden geçme durumunu kontrol eder
    for ogrenci, notu in ogrenci_notlari.items():
        toplam_not += notu  # Toplam notu günceller
        if notu >= gecme_notu:  # Geçme notundan yüksek veya eşitse
            gecenler.append(ogrenci)  # Listeye ekler

    # Sınıfın ortalamasını hesaplar
    sinif_ortalamasi = toplam_not / len(ogrenci_notlari)

    return gecenler, sinif_ortalamasi

# Örnek kullanım
ogrenci_notlari = {'Ayşe': 85, 'Ahmet': 74, 'Mehmet': 45, 'Elif': 90}
gecme_notu = 70
gecenler, ortalama = dersi_gecenler(ogrenci_notlari, gecme_notu)
print("Geçen öğrenciler:", gecenler)
print("Sınıf ortalaması:", ortalama)

# İki string değişkende tutulan sayıların bölünmesi

birinciSayi = "0"
ikinciSayi = "5"

try:
    # String olarak verilen sayılar float tipine çevrilir ve bölme işlemi yapılır
    sonuc = float(birinciSayi) / float(ikinciSayi)
    print(sonuc)  # Sonuç ekrana yazdırılır
except ZeroDivisionError:  # Eğer sıfıra bölme hatası alınırsa
    print("Bir sayı sıfıra bölünemez!")  # Uyarı mesajı ekrana yazdırılır
except Exception as e:  # Diğer tüm hatalar için genel bir yakalama
    print(f"Bir hata oluştu: {e}")
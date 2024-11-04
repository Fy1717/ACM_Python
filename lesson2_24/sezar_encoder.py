alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ'
alfabe_kucuk = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz'

def sezar_sifrele(metin, anahtar):
    sifreli_metin = ""
    for harf in metin:
        if harf.isalpha(): 
            if harf.isupper():
                yeni_index = (alfabe_buyuk.index(harf) + anahtar) % 29
                sifreli_metin += alfabe_buyuk[yeni_index]
            else:
                yeni_index = (alfabe_kucuk.index(harf) + anahtar) % 29
                sifreli_metin += alfabe_kucuk[yeni_index]
        else:
            sifreli_metin += harf  # Harf değilse direkt ekle
    return sifreli_metin

while True:
    metin = input("\n\n\nŞifrelenecek metni girin ('q' tuşuna basarak çıkabilirsiniz): ")
    if metin.lower() == 'q':
        print("Programdan çıkılıyor...")
        break
    anahtar = int(input("Şifreleme anahtarını girin: "))

    sifreli_metin = sezar_sifrele(metin, anahtar)

    print("\nŞifreli Metin:", sifreli_metin)
    
    
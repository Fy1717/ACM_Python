alfabe_buyuk = 'ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ'
alfabe_kucuk = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz'
            
def sezar_sifre_coz(sifreli_metin, anahtar):
    sifresiz_metin = ""
    for harf in sifreli_metin:
        if harf.isalpha(): 
            if harf.isupper():
                yeni_index = (alfabe_buyuk.index(harf) - anahtar) % 29
                sifresiz_metin += alfabe_buyuk[yeni_index]
            else:
                yeni_index = (alfabe_kucuk.index(harf) - anahtar) % 29
                sifresiz_metin += alfabe_kucuk[yeni_index]
        else:
            sifresiz_metin += harf 
            
    return sifresiz_metin

sifreli_metin = input("\n\n\nŞifreli metni girin: ")
anahtar = int(input("Şifreleme anahtarını girin: "))

sifresiz_metin = sezar_sifre_coz(sifreli_metin, anahtar)

print("\nŞifresiz Metin:", sifresiz_metin)

# İsminizdeki sessiz harfleri bir listeye atma

isim = "Furkan"  # İsim değişkeni tanımlanır
sessiz_harfler = []  # Sessiz harfleri saklamak için boş bir liste oluşturulur
index = 0  # While döngüsü için index tanımlanır

# Sessiz harfleri tanımlayan bir string
sessizler = "bcçdfgğhjklmnpqrsştvwxzBCÇDFGĞHJKLMNPQRSŞTVWXZ"

# İsim uzunluğu kadar döngü kurulur
while index < len(isim):
    if isim[index] in sessizler:  # Eğer harf sessizler stringinde varsa
        sessiz_harfler.append(isim[index])  # Liste eklenir
    index += 1

print(sessiz_harfler)  # Sessiz harfler listesi ekrana yazdırılır

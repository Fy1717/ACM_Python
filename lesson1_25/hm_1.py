# 1'den 100'e kadar olan sayılardan asal olanları ekrana yazdırma
for num in range(1, 101):  # 1'den 100'e kadar sayılar üzerinde döngü kurulur
    for i in range(2, num):
        if (num % i) == 0:  # Eğer sayı i'ye tam bölünüyorsa, asal değildir
            break
    else:
        print(num)  # Eğer hiçbir i sayısına tam bölünmüyorsa, sayı asaldır ve yazdırılır

# Belirli bir düzende "acm" kelimesinin çıktısını almak

indent = 0  # Başlangıçta girinti miktarı 0
for i in range(1, 10):  # 9 satır olacak şekilde bir döngü
    if i in [2, 3, 4, 6, 7]:  # Girinti arttırılacak satırlar
        indent += 2
    elif i in [5, 8]:  # Girinti azaltılacak satırlar
        indent -= 2
    print(' ' * indent + 'acm')  # Girinti ve kelimeyi yazdırır

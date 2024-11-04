def death_of_mafia(*fathers_of_mafia): #*args parametresi yerine *fathers_of_mafia kullanıldı.
    """ DOCSTRING of the function // help() fonksiyonu içerisine fonksiyon ismini vererek görüntüleyebiliriz
    
    Verilen mafya babalarının ö**münü ilan eden fonksiyon.

    Args:
        *mafya_babaları: Ö**dürülen mafya babalarının isimleri.
    
    Returns:
        str: Kim bu Polat Alemdar!
    """
    
    for mafia in fathers_of_mafia:
        print(mafia + " öldü.")
        
    return f"\n\nEn son yas tuttuğu gece 6 babayı ö**ürmüş, [{', '.join(fathers_of_mafia)}]"

list_of_mafia = ["Kürt Bedo", "Freud Fethi", "Faris Sarıyayla", "Üstün Kısa", "Demir Görkemli", "Cerrahpaşalı Halit"]

#help(death_of_mafia) # fonksiyonun ne işe yaradığını, hangi parametreleri alıp return ettiği veriyi açıklamalı
print(death_of_mafia(*list_of_mafia))

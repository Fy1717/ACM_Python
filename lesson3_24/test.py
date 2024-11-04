class Saat:
    def __init__(self, isim, model, marka):
        self.isim = isim
        self.model = model
        self.marka = marka
        
    def calculate_calori(self, first_calori, last_calori):
        print("Yakılan kalori : ", last_calori - first_calori)
        
    def marka_yazdir(self):
        print(self.marka)
    
    
#saat = {"isim": "watch 4", "model": "2020", "marka": "apple"}

saat1 = Saat("watch 4", "2020", "apple")
saat2 = Saat("watch 5", "2024", "samsung")


#saat.marka_yazdir()
#saat.calculate_calori(15, 2432)

print(saat1.isim , " ", saat1.marka, " ", saat1.model)
print(saat2.isim , " ", saat2.marka, " ", saat2.model)

#watch 4   apple   2020


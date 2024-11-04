# Hayvan CLASS'I (BASE CLASS)
# 2 ana özellik tanımlandı: (isim ve yaş)
class Hayvan:
    """Hayvan sınıfı, temel hayvan özelliklerini ve davranışlarını tanımlar."""

    def __init__(self, isim, yas):
        """Hayvan sınıfının yapıcı metodu."""
        self.isim = isim
        self.yas = yas

    def konus(self):
        """Hayvanın konuşma davranışını temsil eden metod."""
        return f"Ben {self.isim} ve {self.yas} yaşındayım."
# ------------------------------------------------------------------------------------------------    

# ------------------------------------------------------------------------------------------------    
# Kedi CLASS'I (SUBCLASS)
# Hayvan CLASS'INDAN türetilen bir sınıf
# "tuy_rengi"  özelliği eklendi (kendine özel)
class Kedi(Hayvan):
    """Kedi sınıfı, Hayvan sınıfından türetilmiş bir alt sınıftır."""

    def __init__(self, isim, yas, tuy_rengi):
        """Kedi sınıfının yapıcı metodu."""
        super().__init__(isim, yas) # Hayvan Sınıfındaki Yapıcı Metoda Uyarlandı
        self.tuy_rengi = tuy_rengi

    # @override
    def konus(self):
        """Kedinin konuşma davranışını temsil eden metod."""
        return f"Ben bir kediyim. Adım {self.isim}. Tüy rengim {self.tuy_rengi}. Yaşım {self.yas}."

    def miyavla(self):
        """Kedinin miyavlama davranışını temsil eden metod."""
        return "Miyavlama sesi"
# ------------------------------------------------------------------------------------------------    

# ------------------------------------------------------------------------------------------------    
# Kopek CLASS'I (SUBCLASS)
# Hayvan CLASS'INDAN türetilen bir sınıf
# "turu"  özelliği eklendi (kendine özel)
class Kopek(Hayvan):
    """Köpek sınıfı, Hayvan sınıfından türetilmiş bir alt sınıftır."""

    def __init__(self, isim, yas, turu):
        """Köpek sınıfının yapıcı metodu."""
        super().__init__(isim, yas) # Hayvan Sınıfındaki Yapıcı Metoda Uyarlandı
        self.turu = turu

    # @override
    def konus(self):
        """Köpeğin konuşma davranışını temsil eden metod."""
        return f"Ben bir köpeğim. Adım {self.isim}. Türüm {self.turu}. Yaşım {self.yas}."

    def havla(self):
        """Köpeğin havlama davranışını temsil eden metod."""
        return "Havlama sesi"


kedi = Kedi("Pamuk", 3, "Beyaz")
kopek = Kopek("Buddy", 5, "Golden Retriever")



print(kedi.konus())
print(kopek.konus())
print("\n----------------------------------------------\n")
print(kedi.miyavla())
print(kopek.havla())


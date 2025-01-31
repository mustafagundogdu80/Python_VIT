# Lesson 5 - Date: 25.01.2025
class Kitap():
    Dil = "Türkçe"
    Toplam_kitap_sayisi = 0
    Toplam_sayfa_sayisi = 0
    # Constructor
    def __init__(self ,yazar, kitap_adi,Tur, sayfa_sayisi=0):
        self.yazar = yazar
        self.kitap_adi = kitap_adi
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = Tur
        Kitap.Toplam_kitap_sayisi += 1
        Kitap.Toplam_sayfa_sayisi += sayfa_sayisi
    
    def bilgileri_goster(self):
        print(f"Kitap Adı:{self.kitap_adi}, yazarı: {self.yazar} sayfa sayısı:{self.sayfa_sayisi}")

    def sayfa_ekle(self, sayfa_sayisi):
        Kitap.Toplam_sayfa_sayisi += sayfa_sayisi
        self.sayfa_sayisi += sayfa_sayisi
        
    
    def sayfa_cikar(self, sayfa_sayisi):
        if self.sayfa_sayisi < sayfa_sayisi:
            Kitap.Toplam_sayfa_sayisi -= sayfa_sayisi
            self.sayfa_sayisi -= sayfa_sayisi
        else:
            print("Hatalı işlem")
class Kitap2:
    toplam_sayfa_sayisi = 0
    toplam_kitap = 0
    def __init__(self, adi, yazari, türü, sayfasayisi = 0):
        self.adi = adi
        self.yazari = yazari
        self.tür = türü
        self.sayfa_sayisi = sayfasayisi
        Kitap2.toplam_kitap += 1
        Kitap2.toplam_sayfa_sayisi += sayfasayisi

    def kitap_guncelle(self, sayfasayisi):
        Kitap2.toplam_sayfa_sayisi += sayfasayisi - self.sayfa_sayisi
        self.sayfa_sayisi = sayfasayisi

class Memur():
    def __init__(self, adi, soyadi, maasi):
        self.adi = adi
        self.soyadi = soyadi
        self.maasi = maasi
    
    def kendini_tanit(self):
        print("Adı:", self.adi)
        print("Soyadi:", self.soyadi)
        print("Maaşı: ", self.maasi)

class Yonetici(Memur):
    def __init__(self, adi, soyadi, maasi, birimi):
        super().__init__(adi, soyadi, maasi)
        self.birimi = birimi
        
class Stajer(Memur):
    stajer_maasi = 1000
    def __init__(self, adi, soyadi, egitimi):
        super().__init__(adi, soyadi, Stajer.stajer_maasi)
        self.egitimi = egitimi

class Tasit():
    toplam_tasit_sayisi = 0
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        Tasit.toplam_tasit_sayisi += 1

    def kendini_tanit(self):
        print(self.marka)
        print(self.model)



if __name__ == "__main__":
    print("Kitap 1: ")
    kitap = Kitap("Mustafa", "Hayatim",255)
    kitap.bilgileri_goster()
    kitap.sayfa_ekle(50)
    print(kitap.sayfa_sayisi)
    kitap.sayfa_cikar(100)
    print(kitap.sayfa_sayisi)
    print("------------------------------------")
    print("Kitap 2: ")
    kitap2 = Kitap("Zülfü Livaneli", "Son Ada", 320)
    kitap2.bilgileri_goster()
    kitap2.sayfa_ekle(50)
    print(kitap2.sayfa_sayisi)
    kitap2.sayfa_cikar(100)
    print(kitap.sayfa_sayisi)
    
    print("-------------------------------------")
    print("Kitap 3: ")
    kitap3 = Kitap("Jorge Owel","Hayvan Çiftliği",100)
    kitap3.bilgileri_goster()
    kitap3.sayfa_ekle(50)
    print(kitap3.sayfa_sayisi)
    kitap3.sayfa_cikar(100)
    print(kitap3.sayfa_sayisi)

    print("-------------------------------------")
    print("Memur: ")
    memur1 = Memur("Mustafa", "Gundogdu", 3500)
    memur1.kendini_tanit()
    print("-------------------------------------")
    print("Yonetici: ")
    yonetici1 = Yonetici(memur1.adi,memur1.soyadi,memur1.maasi,"Bilgi İşlem")
    yonetici1.kendini_tanit()
    print("-------------------------------------")
    print("Stajer: ")
    stajer1 = Stajer("Staj", "Er","Lisans")
    stajer1.kendini_tanit()

    print("------------------------------------")
    print("Araç 1:")
    arac1 = Tasit("Honda","Accord")
    arac1.kendini_tanit()
    print("Araç 2:")
    arac2 = Tasit("Toyota","Prius")
    arac2.kendini_tanit()
    print("-------------------------------------")
    print("Toplam Araç sayımız:", Tasit.toplam_tasit_sayisi)

    kitap21 = Kitap2("kitap1","Yazar1","Roman",500)
    kitap22 = Kitap2("kitap2","Yazar2","Roman",400)
    print("Toplam sayfa sayısı: ",Kitap2.toplam_sayfa_sayisi)
    kitap21.kitap_guncelle(300)
    print("Toplam sayfa sayısı: ",Kitap2.toplam_sayfa_sayi)
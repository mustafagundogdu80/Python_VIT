# 1. Bir Sayının Karesini Hesaplama
# Fonksiyon yazmadan ve yazarak bir sayının karesini hesaplayan bir fonksiyon oluşturun.
# Soru:

# Verilen bir sayının karesini hesaplayan bir fonksiyon yazınız. Eğer hiçbir argüman verilmezse, varsayılan olarak 10'un karesini döndürsün.
# Ekstra: Üç farklı sayıyı çarpan bir fonksiyon yazınız ve en az bir argüman belirtmeden çağırın.
def my_square(num=10):
    return num ** 2



# 2. İki Sayıyı Toplama
# İki sayıyı toplamak için bir fonksiyon oluşturun.
# Soru:
def my_sum(a, b):
    return a + b
# topla(a, b) adında bir fonksiyon yazınız. Bu fonksiyon, iki sayıyı toplamalı ve sonucu döndürmelidir.
# 3. Faktöriyel Hesaplama
# Bir sayının faktöriyelini hesaplayan bir fonksiyon yazınız.
# Soru:

# factorial(number) adlı bir fonksiyon yazınız. Bu fonksiyon verilen sayının faktöriyelini hesaplamalıdır. 0 için 1 döndürmelidir.
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# 4. Listede En Büyük Sayıyı Bulma
# Bir liste içindeki en büyük sayıyı bulan bir fonksiyon yazınız.
# Soru:

# en_buyuk_sayi(liste) adlı bir fonksiyon oluşturun. Bu fonksiyon verilen bir listenin içindeki en büyük sayıyı döndürmelidir.
# Örnek Girdi: [2, 3, 1, 7, 4, 2]
# Beklenen Çıktı: 7
# 5. Emeklilik Yaşı Hesaplama
# Kullanıcının yaşı ve cinsiyetine göre emekliliğe kalan yılı hesaplayan bir fonksiyon yazınız.
# Soru:

# emeklilik_yasi_hesapla(kadinMi, yas) fonksiyonunu yazınız.
# Eğer kişi kadınsa, emeklilik yaşı 55.
# Eğer kişi erkekse, emeklilik yaşı 63.
# Kişi emekli olmuşsa, 'Zaten emekli' döndürün.
# 6. Recursive Faktöriyel Hesaplama
# Faktöriyel hesaplamasını bir döngü yerine özyineleme (recursion) kullanarak yapınız.
# Soru:

# recursive_factorial(number) fonksiyonunu yazınız. Bu fonksiyon özyineleme ile faktöriyel hesaplamalıdır.
# 7. Kelimeleri Ters Çevirme
# Bir metindeki her kelimeyi ters çeviren bir sistem oluşturun.
# Soru:

# kelimelere_ayir(metin): Verilen metni kelimelere ayıran bir fonksiyon yazınız.
# kelimeleri_ters_cevir(kelimeler): Kelimeleri ters çeviren bir fonksiyon yazınız.
# yeni_metin_olustur(ters_kelimeler): Ters çevrilmiş kelimelerle yeni bir metin oluşturun.
# Örnek Girdi: "Ali ata bak"
# Beklenen Çıktı: "ilA ata kab"

# 8. Kelime Frekansı Hesaplama
# Bir metindeki kelimelerin kaç kez geçtiğini hesaplayan bir fonksiyon yazınız.
# Soru:

# kelime_frekansi(metin) adlı bir fonksiyon yazınız.
# Örnek Girdi: "bu bir test bu sadece bir test"
# Beklenen Çıktı: {'bu': 2, 'bir': 2, 'test': 2, 'sadece': 1}
# 9. Lambda ile Toplama ve Kare Hesaplama
# Anonim (lambda) fonksiyonlar kullanarak işlemler yapınız.
# Soru:

# İki sayıyı toplayan bir lambda fonksiyonu oluşturun.
# Verilen bir sayının karesini hesaplayan bir lambda fonksiyonu yazınız.
# 10. Bir Listenin Ortalamasını Hesaplama
# Verilen bir listenin ortalamasını hesaplayınız.
# Soru:

# ortalama = lambda liste: sum(liste) / len(liste) şeklinde bir lambda fonksiyonu yazınız.
# Örnek Girdi: [1, 5, 10, 2, 20]
# Beklenen Çıktı: 7.6
# 11. Lambda ile Filtreleme İşlemleri
# Bir liste üzerinde lambda ile filtreleme yapınız.
# Soru:

# Bir listede sadece tek sayıları filtreleyen bir lambda ifadesi yazınız.
# Negatif sayıları filtreleyen bir lambda ifadesi yazınız.
# Örnek Girdi: [-1, 4, 8, 14, -5]
# Beklenen Çıktı: [-1, -5]

# 12. Reduce ile Liste İşlemleri
# Bir listedeki elemanlara toplama ve çarpma işlemi uygulayınız.
# Soru:

# Bir listenin elemanlarının toplamını ve çarpımını reduce kullanarak hesaplayınız.
# Listedeki en büyük sayıyı reduce ile bulunuz.
# Örnek Girdi: [1, 5, 3, 9, 2]
# Beklenen Çıktı:

# Toplam: 20
# Çarpım: 270
# En Büyük: 9

# 13. Fibonacci Dizisi Oluşturma
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, verilen bir sayı kadar Fibonacci dizisi elemanını bir liste olarak döndürsün. Örneğin, fibonacci(10) çağrıldığında 10 elemanlı bir Fibonacci dizisi üretmelidir.

# 14. Bir Sayının Asal Olup Olmadığını Kontrol Etme
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir sayının asal olup olmadığını kontrol etsin ve sonuç olarak True (asal) veya False (asal değil) döndürsün. Örneğin, asal_mi(29) çağrıldığında True, asal_mi(10) çağrıldığında False döndürmelidir.

# 15. Liste Elemanlarını Çift mi Tek mi Diye Ayırma
# Soru:
# Bir liste içindeki elemanları "Çift" veya "Tek" olarak belirten bir fonksiyon yazınız. Fonksiyon, liste elemanlarının sırasına göre "Çift" ya da "Tek" stringlerini döndüren bir liste oluştursun. Örneğin, cift_tek_ayir([1, 2, 3, 4, 5]) çağrıldığında ['Tek', 'Çift', 'Tek', 'Çift', 'Tek'] döndürmelidir.

# 16. Liste Elemanlarını Çift Sayılar ve Tek Sayılar Olarak Gruplama
# Soru:
# Bir listeyi iki ayrı listeye ayıran bir fonksiyon yazınız. İlk liste sadece çift sayıları, ikinci liste ise sadece tek sayıları içermelidir. Fonksiyon bu iki listeyi bir tuple (demet) olarak döndürsün. Örneğin, gruplandir([1, 2, 3, 4, 5]) çağrıldığında ([2, 4], [1, 3, 5]) döndürmelidir.

# 17. Bir Listenin Tersini Döndürme
# Soru:
# Bir listeyi ters çeviren bir fonksiyon yazınız. Örneğin, ters_cevir([1, 2, 3, 4, 5]) çağrıldığında [5, 4, 3, 2, 1] döndürmelidir.

# 18. Bir Listenin Ortalamasını Hesaplama
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir listenin elemanlarının aritmetik ortalamasını hesaplasın ve sonucu döndürsün. Örneğin, liste_ortalama([10, 20, 30]) çağrıldığında 20.0 döndürmelidir.

# 19. Listedeki En Küçük Elemanı Bulma
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir liste içindeki en küçük elemanı döndürsün. Örneğin, en_kucuk([10, 20, 5, 15]) çağrıldığında 5 döndürmelidir.

# 20. Liste İçindeki Harflerin Frekansını Bulma
# Soru:
# Bir string içindeki harflerin frekansını hesaplayan bir fonksiyon yazınız. Fonksiyon, harfleri ve her bir harfin kaç kez tekrar ettiğini bir dictionary (sözlük) olarak döndürmelidir. Örneğin, harf_frekansi("hello world") çağrıldığında {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1} döndürmelidir.
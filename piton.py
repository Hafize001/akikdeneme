def hesapla(x,y):
    """İki sayının toplamını döndüren fonksiyon."""
    return x + y
def carpma(a,b):
    """İki sayının çarpımını döndüren fonksiyon."""
    return a * b
print(hesapla(3, 5))  # Çıktı: 8
print(carpma(4, 6))   # Çıktı: 24

def faktoriyel(n):
    """Bir sayının faktöriyelini döndüren fonksiyon."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)
print(faktoriyel(5))  # Çıktı: 120

def fibonacci(n):
    """Fibonacci dizisindeki n'inci sayıyı döndüren fonksiyon."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))  # Çıktı: 13

def asal_mi(num):
    """Bir sayının asal olup olmadığını kontrol eden fonksiyon."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(asal_mi(11))  # Çıktı: True

def ters_cevir(s):
    """Bir stringi tersine çeviren fonksiyon."""
    return s[::-1]
print(ters_cevir("merhaba"))  # Çıktı: abahrem
def en_büyük(liste):
    """Bir listedeki en büyük sayıyı döndüren fonksiyon."""
    if not liste:
        return None
    en_büyük_sayı = liste[0]
    for sayı in liste:
        if sayı > en_büyük_sayı:
            en_büyük_sayı = sayı
    return en_büyük_sayı

print(en_büyük([3, 5, 2, 8, 1]))  # Çıktı: 8
def ortalama(liste):
    """Bir listedeki sayıların ortalamasını döndüren fonksiyon."""
    if not liste:
        return 0
    toplam = sum(liste)
    return toplam / len(liste)
print(ortalama([4, 8, 15, 16, 23, 42]))  # Çıktı: 18.0
def asal_sayilar(n):
    """n'e kadar olan asal sayıları döndüren fonksiyon."""
    asallar = []
    for num in range(2, n + 1):
        if asal_mi(num):
            asallar.append(num)
    return asallar
print(asal_sayilar(20))  # Çıktı: [2, 3, 5, 7, 11, 13, 17, 19]
def palindrom_mu(s):
    """Bir stringin palindrom olup olmadığını kontrol eden fonksiyon."""
    s = s.replace(" ", "").lower()
    return s == ters_cevir(s)
print(palindrom_mu("A man a plan a canal Panama"))  # Çıktı: True
def liste_tersi(liste):
    """Bir listenin tersini döndüren fonksiyon."""
    return liste[::-1]
print(liste_tersi([1, 2, 3, 4, 5]))  # Çıktı: [5, 4, 3, 2, 1]
def ortak_elemanlar(liste1, liste2):
    """İki listenin ortak elemanlarını döndüren fonksiyon."""
    return list(set(liste1) & set(liste2))
print(ortak_elemanlar([1, 2, 3], [2, 3, 4]))  # Çıktı: [2, 3]
def kareler_toplami(n):
    """1'den n'e kadar olan sayıların karelerinin toplamını döndüren fonksiyon."""
    toplam = 0
    for i in range(1, n + 1):
        toplam += i ** 2
    return toplam
print(kareler_toplami(3))  # Çıktı: 14 (1^2 + 2^2 + 3^2 = 14)
def en_küçük(liste):
    """Bir listedeki en küçük sayıyı döndüren fonksiyon."""
    if not liste:
        return None
    en_küçük_sayı = liste[0]
    for sayı in liste:
        if sayı < en_küçük_sayı:
            en_küçük_sayı = sayı
    return en_küçük_sayı
print(en_küçük([3, 5, 2, 8, 1]))  # Çıktı: 1
def harf_sayisi(s):
    """Bir stringdeki harf sayısını döndüren fonksiyon."""
    sayac = 0
    for char in s:
        if char.isalpha():
            sayac += 1
    return sayac
print(harf_sayisi("Merhaba Dünya! 123"))  # Çıktı: 13
def çarpanlar(n):
    """Bir sayının tüm pozitif çarpanlarını döndüren fonksiyon."""
    çarpan_listesi = []
    for i in range(1, n + 1):
        if n % i == 0:
            çarpan_listesi.append(i)
    return çarpan_listesi
print(çarpanlar(12))  # Çıktı: [1, 2, 3, 4, 6, 12]
def üslü_sayı(tab, üs):
    """Bir sayının üslü halini döndüren fonksiyon."""
    return tab ** üs
print(üslü_sayı(2, 3))  # Çıktı: 8

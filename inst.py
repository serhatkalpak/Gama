import hashlib
import time
from colorama import init, Fore

init(autoreset=True)

def kullaniciya_ozel_numara(kullanici_adi):
    # Kullanıcı adına göre sabit hash değeri al
    hash_degeri = hashlib.md5(kullanici_adi.encode()).hexdigest()
    
    # Hash'i sayıya çevir
    sayisal = ''.join([str(int(c, 16)) for c in hash_degeri if c.isalnum()])
    
    ana_kisim = sayisal[:9]  # İlk 9 hane
    numara = ana_kisim + "31"  # Sonu 31 olacak

    ulke_kodu = "+81"  # Sabit ülke kodu

    return ulke_kodu + " " + numara

def uygulama():
    print(Fore.CYAN + "=== Instagram Numara Bulucu ===\n")

    kullanici = input(Fore.YELLOW + "Instagram kullanıcı adını gir (@ olmadan): ")
    
    tam_numara = kullaniciya_ozel_numara(kullanici)

    yildizli = '*' * (len(tam_numara) - 2) + tam_numara[-2:]

    print(Fore.GREEN + f"\n@{kullanici} kullanıcı adına ait kayıtlı numara bulundu: {yildizli}")
    
    secim = input(Fore.MAGENTA + "\n[1] Numarayı Tara\n\nSeçiminiz: ")

    if secim == "1":
        print(Fore.CYAN + "\nNumara taranıyor...")
        time.sleep(2)
        print(Fore.GREEN + f"\nKayıtlı telefon numarası: {tam_numara}")
    else:
        print(Fore.RED + "\nGeçersiz seçim. Program sonlandırıldı.")

# Başlat
uygulama()

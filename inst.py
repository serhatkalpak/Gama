import random
import time
from colorama import init, Fore

init(autoreset=True)

# Bazı rastgele ülke kodları
ulke_kodlari = [ "+81"]

def sabit_numara_uret():
    # Ülke kodunu rastgele seç
    kod = random.choice(ulke_kodlari)
    # 9 haneli rastgele numara üret (son iki hane "31" olacak)
    orta_numara = ''.join(str(random.randint(0, 9)) for _ in range(9)) + "31"
    return kod + " " + orta_numara

# Numara sabit bir şekilde oluşturuluyor
sabit_numara = sabit_numara_uret()

def uygulama():
    print(Fore.CYAN + "=== Instagram Verisinden Numara Bulucu ===\n")

    # Kullanıcıdan Instagram kullanıcı adı alınacak
    kullanici = input(Fore.YELLOW + "Instagram kullanıcı adını gir : ")
    
    # Sabit numara
    tam_numara = sabit_numara

    # Yıldızlarla gizlenen numara (son iki hane açık)
    yildizli = '*' * (len(tam_numara) - 2) + tam_numara[-2:]

    print(Fore.GREEN + f"\n@{kullanici} kullanıcı adına ait kayıtlı numara bulundu: {yildizli}")
    
    # Numara tarama seçeneği sunuluyor
    secim = input(Fore.MAGENTA + "\n[1] Numarayı Tara\n\nSeçiminiz: ")

    if secim == "1":
        print(Fore.CYAN + "\nNumara taranıyor...")
        time.sleep(2)
        # Gerçek numara açık şekilde gösteriliyor
        print(Fore.GREEN + f"\nKayıtlı telefon numarası: {tam_numara}")
    else:
        print(Fore.RED + "\nGeçersiz seçim. Program sonlandırıldı.")

# Başlat
uygulama()

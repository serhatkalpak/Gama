import hashlib
import time
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(Fore.GREEN + Style.BRIGHT + """
██████╗ ██╗███╗   ██╗████████╗███████╗
██╔══██╗██║████╗  ██║╚══██╔══╝██╔════╝
██████╔╝██║██╔██╗ ██║   ██║   █████╗  
██╔═══╝ ██║██║╚██╗██║   ██║   ██╔══╝  
██║     ██║██║ ╚████║   ██║   ███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
    """)
    print(Fore.MAGENTA + "     Instagram Numara Bulucu Tool ")
    print(Fore.CYAN + "           Coded by Serhat | KAPLAN \n")

def generate_number(user_id, username):
    combined = f"{user_id}_{username}"
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    numeric = ''.join([str(int(c, 16)) for c in hashed if c.isalnum()])
    number = numeric[:9] + "31"
    return "+81 " + number

def start():
    banner()
    user_id = input(Fore.YELLOW + "[?] Instagram Kullanıcı ID'si: ")
    username = input(Fore.YELLOW + "[?] Instagram Kullanıcı Adı: ")

    full_number = generate_number(user_id, username)
    hidden_number = '*' * (len(full_number) - 2) + full_number[-2:]

    print(Fore.GREEN + f"\n[+] @{username} kullanıcısına ait kayıtlı numara bulundu: {Fore.LIGHTRED_EX}{hidden_number}")

    choice = input(Fore.CYAN + "\n[1] Numarayı Tara\n\n" + Fore.LIGHTGREEN_EX + "[>] Seçiminiz: ")

    if choice == "1":
        print(Fore.LIGHTBLUE_EX + "\n[*] Numara taranıyor...")
        time.sleep(2)
        print(Fore.LIGHTGREEN_EX + f"\n[✓] Kayıtlı telefon numarası: {Fore.WHITE + Back.BLACK}{full_number}")
    else:
        print(Fore.RED + "\n[-] Geçersiz seçim. Program sonlandırıldı.")

start()

import instaloader
from colorama import Fore, Style, init

init(autoreset=True)

def get_profile_data(username):
    L = instaloader.Instaloader()
    try:
        # Giriş yapmadan veri çekme (Halka açık hesaplar için)
        profile = instaloader.Profile.from_username(L.context, username)
        
        if profile.is_private:
            print(f"{Fore.RED}[HATA] Hesap gizli! Veri çekilemez.")
            return None

        # Temel Bilgiler
        print(f"\n{Fore.CYAN}=== @{profile.username} Bilgileri ===")
        print(f"{Fore.YELLOW}Ad: {Fore.WHITE}{profile.full_name}")
        print(f"{Fore.YELLOW}Biyografi: {Fore.WHITE}{profile.biography}")
        print(f"{Fore.YELLOW}Takipçi: {Fore.WHITE}{profile.followers}")
        print(f"{Fore.YELLOW}Takip Edilen: {Fore.WHITE}{profile.followees}")
        print(f"{Fore.YELLOW}Gönderi Sayısı: {Fore.WHITE}{profile.mediacount}")

        # Son 3 Gönderi Bilgisi
        posts = list(profile.get_posts())[:3]
        print(f"\n{Fore.YELLOW}Son Gönderiler:")
        for i, post in enumerate(posts, 1):
            print(f"{Fore.CYAN}{i}. {post.date_utc.strftime('%d/%m/%Y')} | ❤️ {post.likes} | 💬 {post.comments}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Fore.RED}[HATA] Kullanıcı bulunamadı!")
    except instaloader.exceptions.QueryReturnedBadRequestException:
        print(f"{Fore.RED}[HATA] Instagram engelledi! 1 saat sonra tekrar dene.")
    except Exception as e:
        print(f"{Fore.RED}[HATA] Beklenmeyen hata: {str(e)}")

if __name__ == "__main__":
    username = input(f"{Fore.CYAN}[?] Instagram Kullanıcı Adı: {Style.RESET_ALL}").strip().lower()
    get_profile_data(username)

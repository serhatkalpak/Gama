import instaloader
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class InstagramAnalyzer:
    def __init__(self):
        self.L = instaloader.Instaloader()
    
    def get_profile(self, username):
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
            if profile.is_private:
                raise Exception(f"{Fore.RED}[!] Bu hesap gizli!")
            return profile
        except Exception as e:
            print(f"{Fore.RED}[!] Hata: {e}{Style.RESET_ALL}")
            exit()

    def analyze_profile(self, profile):
        data = {
            "username": profile.username,
            "full_name": profile.full_name,
            "biography": profile.biography,
            "followers": profile.followers,
            "followees": profile.followees,
            "posts_count": profile.mediacount,
            "is_verified": profile.is_verified,
            "external_url": profile.external_url,
            "engagement_rate": self.calculate_engagement(profile),
            "active_stories": len(self.get_active_stories(profile)),
            "highlight_reels": len(self.get_highlight_reels(profile)),
            "last_post_date": self.get_last_post_date(profile)
        }
        return data

    def calculate_engagement(self, profile):
        total_likes = 0
        total_comments = 0
        posts = list(profile.get_posts())[:12]
        for post in posts:
            total_likes += post.likes
            total_comments += post.comments
        engagement_rate = ((total_likes + total_comments) / (profile.followers or 1)) * 100
        return f"%{engagement_rate:.2f}"

    def get_active_stories(self, profile):
        try: return self.L.get_stories(userids=[profile.userid])[0].get_items()
        except: return []

    def get_highlight_reels(self, profile):
        return profile.get_highlights()

    def get_last_post_date(self, profile):
        for post in profile.get_posts():
            return post.date_utc.strftime("%d/%m/%Y %H:%M")
        return "Bilinmiyor"

def print_report(data):
    print(f"\n{Fore.CYAN}=== RAPOR: @{data['username']} ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Ad: {Fore.WHITE}{data['full_name']}")
    print(f"{Fore.YELLOW}Biyografi: {Fore.WHITE}{data['biography']}")
    print(f"{Fore.YELLOW}Takipçi: {Fore.WHITE}{data['followers']}")
    print(f"{Fore.YELLOW}Takip Edilen: {Fore.WHITE}{data['followees']}")
    print(f"{Fore.YELLOW}Gönderi Sayısı: {Fore.WHITE}{data['posts_count']}")
    print(f"{Fore.YELLOW}Etkileşim Oranı: {Fore.WHITE}{data['engagement_rate']}")
    print(f"{Fore.YELLOW}Aktif Hikaye: {Fore.WHITE}{data['active_stories']} adet")
    print(f"{Fore.YELLOW}Highlight: {Fore.WHITE}{data['highlight_reels']} adet")
    print(f"{Fore.YELLOW}Son Gönderi: {Fore.WHITE}{data['last_post_date']}")

if __name__ == "__main__":
    analyzer = InstagramAnalyzer()
    username = input(f"{Fore.CYAN}[?] Instagram Kullanıcı Adı: {Style.RESET_ALL}").strip()
    
    try:
        profile = analyzer.get_profile(username)
        data = analyzer.analyze_profile(profile)
        print_report(data)
        print(f"\n{Fore.MAGENTA}[!] Analiz tamamlandı. Çıkış yapılıyor...{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Hata: {e}{Style.RESET_ALL}")

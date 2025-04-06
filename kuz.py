from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import track
import time, requests, os

console = Console()

def banner():
    os.system("clear")
    ascii_text = """
 █████╗ ███╗   ██╗███████╗████████╗ █████╗ 
██╔══██╗████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
███████║██╔██╗ ██║█████╗     ██║   ███████║
██╔══██║██║╚██╗██║██╔══╝     ██║   ██╔══██║
██║  ██║██║ ╚████║███████╗   ██║   ██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
"""
    console.print(f"[bold magenta]{ascii_text}[/bold magenta]")
    console.print(Panel.fit("[bold cyan]Instagram Bilgi Aracı[/bold cyan]\n[green]Etik testler ve güvenlik denetimi için geliştirilmiştir.[/green]", title="[bold yellow]Termux v1.0[/bold yellow]", subtitle="by @yourteam"))

def loading(msg):
    for _ in track(range(20), description=f"[bold cyan]{msg}[/bold cyan]"):
        time.sleep(0.03)

def menu():
    table = Table(show_lines=True, box=None)
    table.add_column("Seçim", justify="center", style="bold yellow")
    table.add_column("Açıklama", style="white")
    table.add_row("1", "Instagram kullanıcı adıyla bilgi sorgula")
    table.add_row("2", "Çıkış yap")
    console.print(table)

def fetch_info(username):
    api_url = f"https://your-api-endpoint.com/lookup?user={username}"
    try:
        loading("Sorgulanıyor...")
        res = requests.get(api_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            email = data.get("email", "[red]Bulunamadı[/red]")
            phone = data.get("phone", "[red]Bulunamadı[/red]")
            panel = Panel.fit(f"[bold green]Kullanıcı:[/bold green] {username}\n[bold green]E-Posta:[/bold green] {email}\n[bold green]Telefon:[/bold green] {phone}", title="Sonuç", subtitle="API Yanıtı", border_style="bright_blue")
            console.print(panel)
        else:
            console.print("[bold red]Geçersiz kullanıcı adı veya API hatası.[/bold red]")
    except:
        console.print("[bold red]Bağlantı kurulamadı. İnternet veya API sorunlu olabilir.[/bold red]")

def main():
    while True:
        banner()
        menu()
        choice = Prompt.ask("[bold yellow]Seçiminiz[/bold yellow]")
        if choice == "1":
            username = Prompt.ask("[bold cyan]Instagram kullanıcı adı[/bold cyan]")
            fetch_info(username)
            input("\n[bold green]Devam etmek için ENTER'a bas[/bold green]")
        elif choice == "2":
            console.print(Panel("[bold green]Çıkış yapılıyor, görüşmek üzere.[/bold green]", border_style="green"))
            break
        else:
            console.print("[red]Geçersiz seçim, tekrar deneyin.[/red]")

if __name__ == "__main__":
    main()

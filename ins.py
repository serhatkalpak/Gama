import os
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.align import Align

console = Console()

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    ascii = """\n
 ██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗███████╗ ██████╗ 
 ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔═══██╗
 ██║██╔██╗ ██║█████╗     ██║   ███████║██╔██╗ ██║█████╗  ██║   ██║
 ██║██║╚██╗██║██╔══╝     ██║   ██╔══██║██║╚██╗██║██╔══╝  ██║   ██║
 ██║██║ ╚████║███████╗   ██║   ██║  ██║██║ ╚████║███████╗╚██████╔╝
 ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ 
"""
    console.print(Align.center(f"[bold magenta]{ascii}[/bold magenta]"))
    console.print(Align.center("[bold cyan]Instagram Bilgi Sorgu Aracı v1.0[/bold cyan]"))
    console.print(Align.center("[green]Etik kullanım için geliştirilmiştir.[/green]\n"))

def menu():
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Seçenek", justify="center")
    table.add_column("Açıklama", justify="left")
    table.add_row("1", "Kullanıcı adıyla sorgu yap")
    table.add_row("2", "Çıkış yap")
    console.print(table)

def get_info(username):
    api_url = f"https://your-api-endpoint.com/lookup?user={username}"
    try:
        console.print("\n[bold yellow]Sorgulanıyor, lütfen bekleyin...[/bold yellow]\n")
        time.sleep(1)
        res = requests.get(api_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            email = data.get("email", "[red]Bulunamadı[/red]")
            phone = data.get("phone", "[red]Bulunamadı[/red]")
            result_panel = Panel.fit(
                f"[bold green]Kullanıcı:[/bold green] {username}\n"
                f"[bold green]E-posta:[/bold green] {email}\n"
                f"[bold green]Telefon:[/bold green] {phone}",
                title="[cyan]Sorgu Sonucu[/cyan]",
                border_style="bright_blue"
            )
            console.print(result_panel)
        else:
            console.print("[red]Kullanıcı bulunamadı ya da API hatalı.[/red]")
    except Exception as e:
        console.print(f"[bold red]Hata oluştu:[/bold red] {e}")

def main():
    while True:
        clear()
        banner()
        menu()
        choice = Prompt.ask("\n[bold yellow]Bir seçenek giriniz[/bold yellow]")
        if choice == "1":
            username = Prompt.ask("[cyan]Instagram kullanıcı adı[/cyan]")
            get_info(username)
            input("\nDevam etmek için Enter'a bas...")
        elif choice == "2":
            console.print("\n[bold green]Çıkış yapılıyor...[/bold green]")
            break
        else:
            console.print("[red]Geçersiz seçim![/red]")
            time.sleep(1)

if __name__ == "__main__":
    main()

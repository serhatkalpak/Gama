import os
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.align import Align

console = Console()

# API ayarları (DÜZENLEMEN GEREKİYOR!)
API_BASE = "https://your-api-endpoint.com/lookup"  # ❌ Default değer çalışmaz

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    ascii_art = """\n
 ██╗███╗   ██╗███████╗████████╗ █████╗ ███╗   ██╗███████╗ ██████╗ 
 ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔════╝██╔═══██╗
 ██║██╔██╗ ██║█████╗     ██║   ███████║██╔██╗ ██║█████╗  ██║   ██║
 ██║██║╚██╗██║██╔══╝     ██║   ██╔══██║██║╚██╗██║██╔══╝  ██║   ██║
 ██║██║ ╚████║███████╗   ██║   ██║  ██║██║ ╚████║███████╗╚██████╔╝
 ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ 
"""
    console.print(Align.center(f"[bold magenta]{ascii_art}[/bold magenta]"))
    console.print(Align.center("[bold cyan]Instagram Bilgi Sorgu Aracı v2.0[/bold cyan]"))
    console.print(Align.center("[green]Etik kullanım için geliştirilmiştir.[/green]\n"))

def menu():
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Seçenek", justify="center")
    table.add_column("Açıklama", justify="left")
    table.add_row("1", "Bilgi Sorgula")
    table.add_row("2", "Çıkış Yap")
    console.print(table)

def check_api_status():
    return API_BASE != "https://your-api-endpoint.com/lookup"

def get_search_type():
    console.print("\n[bold]Arama Türünü Seçin:[/bold]")
    console.print("1: Kullanıcı Adı")
    console.print("2: E-posta Adresi")
    console.print("3: Telefon Numarası")
    return Prompt.ask("Seçiminiz (1-3)", choices=["1", "2", "3"], default="1")

def get_info():
    # API kontrolü
    if not check_api_status():
        console.print(Panel.fit("[bold red]API GEÇERSİZ![/bold red]\nLütfen 'API_BASE' değerini düzenleyin.",
                            border_style="red"))
        return

    # Arama türü seçimi
    search_type = get_search_type()
    
    # Parametrelerin belirlenmesi
    param_map = {
        "1": ("user", "[cyan]Instagram kullanıcı adı[/cyan]"),
        "2": ("email", "[cyan]E-posta adresi[/cyan]"), 
        "3": ("phone", "[cyan]Telefon numarası[/cyan]")
    }
    param, prompt_text = param_map[search_type]
    value = Prompt.ask(prompt_text)

    try:
        console.print("\n[bold yellow]Sorgulanıyor, lütfen bekleyin...[/bold yellow]\n")
        time.sleep(1)
        
        # API isteği
        api_url = f"{API_BASE}?{param}={value}"
        res = requests.get(api_url, timeout=10)
        
        if res.status_code == 200:
            data = res.json()
            result_text = (
                f"[bold green]Arama Türü:[/bold green] {param}\n"
                f"[bold green]Değer:[/bold green] {value}\n"
                f"[bold green]E-posta:[/bold green] {data.get('email', '[red]Bulunamadı[/red]')}\n" 
                f"[bold green]Telefon:[/bold green] {data.get('phone', '[red]Bulunamadı[/red]')}"
            )
            console.print(Panel.fit(result_text, title="[cyan]Sorgu Sonucu[/cyan]", border_style="bright_blue"))
        else:
            console.print(Panel.fit(f"[red]Hata Kodu: {res.status_code}[/red]\nGeçersiz yanıt alındı.", 
                                border_style="red"))

    except Exception as e:
        console.print(Panel.fit(f"[bold red]Hata:[/bold red] {str(e)}", border_style="red"))

def main():
    while True:
        clear()
        banner()
        menu()
        choice = Prompt.ask("\n[bold yellow]Seçiminiz[/bold yellow]", choices=["1", "2"], default="1")
        
        if choice == "1":
            get_info()
            input("\nDevam etmek için Enter'a bas...")
        else:
            console.print("\n[bold green]Çıkış yapılıyor...[/bold green]")
            break

if __name__ == "__main__":
    main()

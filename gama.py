#!/data/data/com.termux/files/usr/bin/python3
import os
import requests
import argparse

# !!! GÜVENLİK UYARISI !!!
# API ANAHTARINIZI ASLA KOD İÇİNDE SAKLAMAYIN!
# BU ÖRNEK SADECE EĞİTİM AMAÇLIDIR.

# API Konfigürasyonu
DEEPSEEK_API_KEY = "sk-e2e655cb26a24003ab9ac98d2bd66245"  # ⚠️ GERÇEK PROJELERDE .env KULLANIN!
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
MODELS = {
    "1": "deepseek-chat",
    "2": "deepseek-coder"
}

def deepseek_chat(prompt, model, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Hata: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="DeepSeek Terminal AI")
    parser.add_argument('-m', '--model', choices=['chat', 'coder'], help='Model seçimi: chat veya coder')
    args = parser.parse_args()

    # Model seçimi
    model = MODELS["1"]  # Varsayılan model
    if args.model:
        model = f"deepseek-{args.model}"
    else:
        print("\n".join([f"{k}. {v}" for k, v in MODELS.items()]))
        model_choice = input("Model seçin (1/2): ")
        model = MODELS.get(model_choice, model)

    print("\n🌟 DeepSeek Terminal AI (Çıkmak için CTRL+C)")
    try:
        while True:
            prompt = input("\nYou: ")
            if prompt.lower() in ['exit', 'quit']: break
            
            print("AI: ", end="", flush=True)
            response = deepseek_chat(prompt, model)
            print(response)
            
    except KeyboardInterrupt:
        print("\nÇıkılıyor...")

if __name__ == "__main__":
    main()

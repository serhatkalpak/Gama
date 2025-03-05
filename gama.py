#!/data/data/com.termux/files/usr/bin/python3
import os
import requests
import argparse
from getpass import getpass

# DeepSeek API Endpoint ve Modeller
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
MODELS = {
    "1": "deepseek-chat",
    "2": "deepseek-coder"
}

def get_api_key():
    """API anahtarını config dosyasından veya kullanıcıdan al"""
    config_path = os.path.expanduser("~/.deepseek_config")
    try:
        with open(config_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        api_key = getpass("🔑 DeepSeek API anahtarınızı girin: ")
        with open(config_path, "w") as f:
            f.write(api_key)
        os.chmod(config_path, 0o600)
        return api_key

def deepseek_chat(prompt, model, api_key, temperature=0.7):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Hata: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="DeepSeek Terminal AI")
    parser.add_argument('-m', '--model', choices=['chat', 'coder'], help='Model seçimi: chat veya coder')
    args = parser.parse_args()

    # Model seçimi
    if not args.model:
        print("\n".join([f"{k}. {v}" for k, v in MODELS.items()]))
        model_choice = input("Model seçin (1/2): ")
        model = MODELS.get(model_choice, MODELS["1"])
    else:
        model = "deepseek-" + args.model

    api_key = get_api_key()
    
    print("\n🌟 DeepSeek Terminal AI (Çıkmak için 'exit' yazın)")
    while True:
        try:
            prompt = input("\nYou: ")
            if prompt.lower() in ['exit', 'quit']:
                break
                
            print("AI: ", end="", flush=True)
            
            # Stream benzeri efekt
            response = deepseek_chat(prompt, model, api_key)
            for line in response.split('\n'):
                print(line)
                
        except KeyboardInterrupt:
            print("\nÇıkılıyor...")
            break

if __name__ == "__main__":
    main()

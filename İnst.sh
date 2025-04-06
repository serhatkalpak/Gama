#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\e[1;36m[+] Termux Aracı Kuruluyor...\e[0m"
pkg update -y && pkg install python -y > /dev/null
pip install requests rich > /dev/null
mkdir -p ~/instainfo
cd ~/instainfo

curl -s -o instainfo.py https://yourdomain.com/path-to/instainfo.py

echo -e "\nalias instainfo='cd ~/instainfo && python instainfo.py'" >> ~/.bashrc
source ~/.bashrc

echo -e "\e[1;32m[✓] Kurulum tamamlandı. Kullanmak için sadece:\e[0m \e[1;33minstainfo\e[0m"

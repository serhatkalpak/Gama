#!/data/data/com.termux/files/usr/bin/bash

echo "==============================="
echo "  INSTAGRAM NUMARA BULUCU KURULUYOR"
echo "===============================

"

# Python ve pip kur
pkg update -y && pkg upgrade -y
pkg install python -y

# pip güncelle
pip install --upgrade pip

# colorama kütüphanesini kur
pip install colorama

# Dosya kontrolü ve çalıştırma
if [ -f "inst.py" ]; then
    echo "inst.py bulundu. Çalıştırılıyor..."
    python inst.py
else
    echo "HATA: inst.py dosyası bulunamadı!"
    echo "Lütfen bu bash scripti ile aynı klasöre inst.py dosyasını yerleştir."
fi

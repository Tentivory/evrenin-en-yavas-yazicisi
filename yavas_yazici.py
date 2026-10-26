#!/usr/bin/env python3
import time
import sys

def yavas_yaz(metin, gecikme=0.5):
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()  # satır sonu

if __name__ == "__main__":
    mesaj = "Bu mesaj o kadar yavaş yazılıyor ki, bitmeden önce yaşlanabilirsiniz. Sabır taşı olun."
    print("Yavaş yazıcı başlıyor...")
    yavas_yaz(mesaj)
    print("Bitti. Tebrikler, hayatta kaldınız.")

# Gizli not: base64 ile saklı siyasi eşitlik mesajı
# QnVrw7x2cmFzaSB5YXZhxZ90xLFyxLFyIGFtYSBmaWtyaW5kZXIgZXNpdCBiYWhhbmUgw7xyZXRpci4=

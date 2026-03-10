#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ARM Donanım Tanı Aracı - İlk Prototip
ÇalıPardusLab1 / Pardus Hata Yakalama ve Öneri Yarışması 2026

Bu araç, Pardus ARM64 sistemlerde temel donanım ve sistem bilgilerini
göstermek amacıyla hazırlanmış ilk prototiptir.
"""

import os
import platform
import shutil


def baslik_yaz() -> None:
    print("=" * 60)
    print("PARDUS ARM DONANIM TANI ARACI")
    print("=" * 60)
    print("ARM tabanlı cihazlar için temel sistem özeti\n")


def sistem_bilgisi_goster() -> None:
    print("[Sistem Bilgisi]")
    print(f"İşletim Sistemi : {platform.system()} {platform.release()}")
    print(f"Mimari          : {platform.machine()}")
    print(f"Platform        : {platform.platform()}")
    print()


def islemci_bilgisi_goster() -> None:
    print("[İşlemci Bilgisi]")
    print(f"İşlemci Türü    : {platform.processor() or 'Bilinmiyor'}")

    model_adi = "Bilinmiyor"
    try:
        with open("/proc/cpuinfo", "r", encoding="utf-8", errors="ignore") as dosya:
            for satir in dosya:
                if "model name" in satir.lower() or "hardware" in satir.lower():
                    model_adi = satir.split(":", 1)[-1].strip()
                    break
    except FileNotFoundError:
        pass

    print(f"Model           : {model_adi}")
    print()


def bellek_bilgisi_goster() -> None:
    print("[Bellek Bilgisi]")
    try:
        with open("/proc/meminfo", "r", encoding="utf-8", errors="ignore") as dosya:
            ilk_satirlar = [next(dosya).strip() for _ in range(3)]
        for satir in ilk_satirlar:
            print(satir)
    except Exception:
        print("Bellek bilgisi alınamadı.")
    print()


def disk_bilgisi_goster() -> None:
    print("[Disk Bilgisi]")
    try:
        toplam, kullanilan, bos = shutil.disk_usage("/")
        print(f"Toplam Alan     : {toplam // (1024**3)} GB")
        print(f"Kullanılan Alan : {kullanilan // (1024**3)} GB")
        print(f"Boş Alan        : {bos // (1024**3)} GB")
    except Exception:
        print("Disk bilgisi alınamadı.")
    print()


def ag_bilgisi_goster() -> None:
    print("[Ağ Bilgisi]")
    try:
        arayuzler = os.listdir("/sys/class/net")
        for arayuz in arayuzler:
            print(f"- {arayuz}")
    except Exception:
        print("Ağ arayüz bilgisi alınamadı.")
    print()


def menu_goster() -> None:
    print("Lütfen bir işlem seçin:")
    print("1 - Tüm sistem özetini göster")
    print("2 - Sistem bilgisini göster")
    print("3 - İşlemci bilgisini göster")
    print("4 - Bellek bilgisini göster")
    print("5 - Disk bilgisini göster")
    print("6 - Ağ bilgisini göster")
    print("7 - Çıkış")
    print()


def tum_ozeti_goster() -> None:
    sistem_bilgisi_goster()
    islemci_bilgisi_goster()
    bellek_bilgisi_goster()
    disk_bilgisi_goster()
    ag_bilgisi_goster()


def ana_program() -> None:
    baslik_yaz()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            tum_ozeti_goster()
        elif secim == "2":
            sistem_bilgisi_goster()
        elif secim == "3":
            islemci_bilgisi_goster()
        elif secim == "4":
            bellek_bilgisi_goster()
        elif secim == "5":
            disk_bilgisi_goster()
        elif secim == "6":
            ag_bilgisi_goster()
        elif secim == "7":
            print("\nProgram sonlandırıldı.")
            break
        else:
            print("\nGeçersiz seçim yaptınız. Lütfen tekrar deneyin.\n")


if __name__ == "__main__":
    ana_program()

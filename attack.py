import os
import sys
import time

def clear_screen():
    # Bersihkan layar terminal
    os.system('clear')  # 'clear' untuk Kali Linux dan Termux

def print_ascii_art():
    # Menampilkan ASCII Art yang baru dengan warna gold (kuning emas)
    print("\033[1;33m")  # Warna gold (kuning emas)
    print("""
┳   ┓  ┓┏    ┏┓      
┃┏┓┏┫┏┓┣┫┏┓┓┏┗┓┏┓┏   
┻┛┗┗┻┗┛┛┗┗┻┛┗┗┛┗ ┗   
┳┓       •  ┏┳   ┓  ┓
┣┫┏┓┏┓╋┏┓┓   ┃┓┏┏┫┏┓┃
┻┛┗┻┛┗┗┗┻┗  ┗┛┗┻┗┻┗┛┗
    """)
    print("\033[0m")  # Reset warna setelah ASCII art

def print_disclaimer():
    # Menampilkan disclaimer
    print("\033[91mDISCLAMER!.....GUNAKAN ALAT INI DENGAN BIJAK...\033[0m")

def attack_mode_1():
    # Bersihkan layar terminal
    clear_screen()

    # Menampilkan notifikasi untuk ATTACK MODE 1
    print("\033[91mUNTUK PENYERANGAN MODE 1 MASUKAN INPUT PERINTAH:\033[0m")
    print("\033[92mpython attack.py\033[0m")

    # Exit program otomatis setelah menampilkan notifikasi
    sys.exit()

def attack_mode_2():
    # Bersihkan layar terminal
    clear_screen()

    # Menampilkan notifikasi untuk ATTACK MODE 2
    print("\033[91mUNTUK MENJALANKAN MODE 2 INI HARAP MEMASUKAN INPUT BERIKUT: \033[0m")
    print("\033[92mgo run attack.go --site https://target.com\033[0m")

    # Exit program otomatis setelah menampilkan notifikasi
    sys.exit()

def menu():
    # Tampilkan ASCII art dan disclaimer
    print_ascii_art()
    print_disclaimer()

    while True:
        # Menampilkan menu dengan warna lime (hijau muda menyala)
        print("\033[1;32m\nMenu Pilihan:")
        print("1. ATTACK MODE 1")
        print("2. ATTACK MODE 2")
        print("3. Keluar\n\033[0m")
        
        # Input pilihan menggunakan angka 1 atau 2
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            attack_mode_1()  # Menjalankan mode 1
        elif choice == "2":
            attack_mode_2()  # Menjalankan mode 2
        elif choice == "3":
            print("Keluar dari program...")
            sys.exit()  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan pilih opsi 1, 2, atau 3.")

if __name__ == "__main__":
    menu()

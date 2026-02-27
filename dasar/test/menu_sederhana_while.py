"""
Menu Sederhana dengan While
"""
try:
    while True:
        print("Menu")
        print("1. Nasi Goreng")
        print("2. Mie Goreng")
        print("3. Ayam Bakar")
        print("4. Es Teh")
        print("5. Keluar")
        pilihan = int(input("Masukkan pilihan Anda: "))
        if pilihan == 1:
            print("Anda memilih Nasi Goreng")
        elif pilihan == 2:
            print("Anda memilih Mie Goreng")
        elif pilihan == 3:
            print("Anda memilih Ayam Bakar")
        elif pilihan == 4:
            print("Anda memilih Es Teh")
        elif pilihan == 5:
            break
        else:
            print("Pilihan tidak ada")
except ValueError:
    print("Pilihan harus berupa angka")
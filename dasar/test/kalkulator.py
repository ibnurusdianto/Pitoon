"""
Aplikasi Kalkulator Sederhana 
"""

print(f"===== KALKULATOR SEDERHANA =====")

while True:
    print("\nPilih operasi : ")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = int(input("Masukan pilihan : "))

    if pilihan == 5:
        break

    angka1 = int(input("Masukan angka pertama : "))
    angka2 = int(input("Masukan angka kedua : "))

    if pilihan == 1:
        print("Hasil : ", angka1 + angka2)
    elif pilihan == 2:
        print("Hasil : ", angka1 - angka2)
    elif pilihan == 3:
        print("Hasil : ", angka1 * angka2)
    elif pilihan == 4:
        print("Hasil : ", angka1 / angka2)
    else:
        print("Pilihan tidak ada")

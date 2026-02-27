harga = 0 
jumlah = 0 
total = 0 

print("===== Warung Sederhana =====")
print("1. Nasi Goreng - Rp 15.000")
print("2. Mie Goreng - Rp 12.000")
print("3. Ayam Bakar - Rp 25.000")
print("4. Es Teh - Rp 5.000")
print("5. Keluar")

while True:
    pilihan = int(input("Masukkan pilihan Anda: "))
    if pilihan == 1:
        harga = 15000
        jumlah = int(input("Masukkan jumlah: "))
        total += harga * jumlah
        print("Total harga: Rp", total)
    elif pilihan == 2:
        harga = 12000
        jumlah = int(input("Masukkan jumlah: "))
        total += harga * jumlah
        print("Total harga: Rp", total)
    elif pilihan == 3:
        harga = 25000
        jumlah = int(input("Masukkan jumlah: "))
        total += harga * jumlah
        print("Total harga: Rp", total)
    elif pilihan == 4:
        harga = 5000
        jumlah = int(input("Masukkan jumlah: "))
        total += harga * jumlah
        print("Total harga: Rp", total)
    elif pilihan == 5:
        break
    else:
        print("Pilihan tidak ada")
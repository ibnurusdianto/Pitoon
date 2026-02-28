"""
Diberikan sebuah list bilangan bulat, tampilkan tiga nilai: min, max, dan rata-rata (dalam float, dibulatkan ke 2 angka di belakang koma).
"""

print(f"===== HITUNG STATISTIK =====")

list = []
while True:
    data = input("Masukan data (selesai untuk selesai) : ")
    if data == "selesai":
        break
    list.append(int(data))
    print(f"Data {data} berhasil ditambahkan")

print(f"===== DATA LIST =====")
print(list)

print(f"===== HITUNG STATISTIK =====")
print(f"Min : {min(list)}")
print(f"Max : {max(list)}")
print(f"Rata-rata : {sum(list) / len(list):.2f}")
"""
Berikut contoh program yaitu menghitung kelulusan
"""

try:
    nilai = int(input("Masukkan nilai (0-100) : "))
    if nilai >= 75:
        print("Lulus")
    elif nilai < 40:
        print("Anda, perlu bimbingan tambahan")
    else:
        print("Tidak lulus")
except ValueError:
    print("Nilai harus berupa angka")
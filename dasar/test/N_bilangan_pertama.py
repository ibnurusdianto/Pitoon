"""
Menjumlahkan N Bilangan Pertama
"""

try:
    n = int(input("Masukkan N: "))
    jumlah = 0
    for i in range(1, n+1):
        jumlah += i
    print("Jumlah N bilangan pertama: ", jumlah)
except ValueError:
    print("N harus berupa angka")
"""
Mengulang salam 
"""

try:
    salam = input("Masukan jumlah salam : ")
    for i in range(int(salam)):
        print("Salam")
except ValueError:
    print("Jumlah salam harus berupa angka")
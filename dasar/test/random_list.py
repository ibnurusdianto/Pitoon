"""
Random data list, list di inputkan oleh pengguna, jika list ditambahkan maka masuk ke dalam list, lalu jika selesai
apakah ingin di print secara acak atau tidak? jika iya maka akan menampilkan acak dari list tersebut,
jika tidak keluar
"""

import random 

print(f"===== RANDOM DATA LIST =====")

list = []
while True:
    data = input("Masukan data (selesai untuk selesai) : ")
    if data == "selesai":
        break
    list.append(data)
    print(f"Data {data} berhasil ditambahkan")

print(f"===== DATA LIST =====")
print(list)

print(f"===== DATA LIST RANDOM =====")
print(random.sample(list, len(list))) # menampilkan data list secara acak

# berikut menampilkan data list secara acak hanya 3 data
print(random.sample(list, 3)) # menampilkan data list secara acak hanya 3 data
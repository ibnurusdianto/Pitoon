"""
For else python 
"""


list_nama = ["heru", "ibnu", "budi", "siti", "ani"]

nama = str(input("Masukan nama yang ingin dicari : "))

for i in list_nama: # tampilkan nama
    if i == nama: # jika i == nama_target maka akan di break
        print(f"nama ditemukan, nama yang dicari yaitu {i}")
        break
    else: # jika i != nama_target maka akan di eksekusi
        print("nama tidak ditemukan")

print("selesai") # selesai


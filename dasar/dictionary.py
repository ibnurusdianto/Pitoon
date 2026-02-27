"""
Dictionary
"""

mahasiswa = {
    "nama" : "ibnu",
    "nim" : "123456789",
    "jurusan" : "informatika"
}

print(f"dictionary : ", mahasiswa)

print(f"nama : ", mahasiswa["nama"])
print(f"nim : ", mahasiswa["nim"])
print(f"jurusan : ", mahasiswa["jurusan"])

print(f"-" * 10)

# menambahkan data ke dalam dictionary
mahasiswa["ipk"] = 3.5
print(f"dictionary : ", mahasiswa)

print(f"-" * 10)

# mengubah data dalam dictionary
mahasiswa["nama"] = "heru"
print(f"dictionary : ", mahasiswa)

print(f"-" * 10)

# menghapus data dalam dictionary
mahasiswa.pop("nim")
print(f"dictionary : ", mahasiswa)

print(f"-" * 10)

# menghitung jumlah index 
print(len(mahasiswa))

print("-" * 10)

# menghapus data paling akhir
print(mahasiswa)

print("-" * 10)

# keys and value 
for i, key in mahasiswa.items():
    print(i, "=", key)
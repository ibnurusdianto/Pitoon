"""
Set Python
"""

names = {"ibnu", "budi", "joko", "siti", "ani"}
print(f"set : ", names)

print(f"-" * 10)

# menambahkan data ke dalam set
names.add("joko")
print(f"set : ", names)

print(f"-" * 10)

# mengubah data dalam set
names.remove("ibnu")
print(f"set : ", names)

print(f"-" * 10)

# menghapus data dalam set
names.remove("ibnu")
print(f"set : ", names)

print(f"-" * 10)

# menghitung jumlah index 
print(len(names))

print("-" * 10)

# menghapus data paling akhir
print(names)
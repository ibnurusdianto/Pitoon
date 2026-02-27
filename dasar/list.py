"""
Manipulasi List 
"""

names = ["ibnu", "budi", "joko", "siti", "ani"]
print(f"list : ", names)

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"-" * 10)

# menambahkan data ke dalam list
names.append("joko")
print(f"list : ", names)

print(f"-" * 10)

# mengubah data dalam list
names[0] = "ibnu"
print(f"list : ", names)

print(f"-" * 10)

# menghapus data dalam list
names.remove("ibnu")
print(f"list : ", names)

print(f"-" * 10)

# menghitung jumlah index 
print(len(names))

print("-" * 10)

# menghapus data paling akhir
print(names)

names.pop()
print(f"list : ", names)


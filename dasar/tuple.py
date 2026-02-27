"""
Tuple
"""

names = ("ibnu", "budi", "joko", "siti", "ani")
print(f"tuple : ", names)

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

print(f"-" * 10)

tanggal_lahir = (19, 8, 2004)
print(f"tanggal lahir : ", tanggal_lahir) 

for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])

print("-" * 10)

# menggunakan for each
for tanggal in tanggal_lahir:
    print(tanggal)


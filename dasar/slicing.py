"""
Belajar Slicing Python

Objek[start:stop:step]

start : index awal
stop : index akhir
step : interval
"""

# contoh mempunyai variable nama 
nama = "ibnu" 
# lalu saya ingin panggil satu persatu index dari variable nama
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])  


"""
seperti yang diketahui, index dihitung dari 0 sampai n-1 
"""

print(f"===== Batas =====")

data = "Hello World"
print(data)
# contoh kita mengakses kata hel, berarti 
print(data[0:3])
# contoh kita mengakses kata world, berarti 
print(data[6:11])
# contoh kita mengakses llo wo
print(data[2:8])
# contooh misal hello 
print(data[:5])
# contoh misal world
print(data[6:])

data2 = "ibnu"
# inut 
print(data2[0:3:1])
# contoh misal inu
print(data2[0] + data2[2:])



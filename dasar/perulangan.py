"""
Perulangan pada python
"""

# for loop
# mencetak angka 0 sampai 5 
for i in range(5):
    print(i) 
    
print("-" * 10)
    
# mencetak angka 1 sampai 10 
for i in range(1, 11): # inget index mulai dari 0, jadi untuk mencapai 10 maka harus di tambah 1
    print(i)

print("-" * 10)

# mencetak angka 1 sampai 10 dengan step 2
for i in range(1, 11, 2): # 2 adalah step, artinya setiap perulangan akan di tambah 2
    print(i)
    
print("-" * 10)

# for loop string 
nama = "ibnu"
for i in nama:
    print(i)
    
print("-" * 10)

# for loop list 
nama = ["ibnu", "budi", "joko", "siti", "ani"]
for i in nama:
    print(i)
    
print("-" * 10)

# for loop list dengan index 
nama = ["ibnu", "budi", "joko", "siti", "ani"]
for i in range(len(nama)):
    print(i, nama[i])
    
print("-" * 10)

# for loop list dengan index dan value 
nama = ["ibnu", "budi", "joko", "siti", "ani"]
for i, nama in enumerate(nama):
    print(i, nama)



# jika kita menggunakan perulangan, kita juga bisa konversi perulangan tersebut ke dalam bentuk list 
number = range(5)
print(f"i : ", list(number))





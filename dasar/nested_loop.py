max = int(input("jumlah bintang: "))

for i in range(max):
    for j in range(0, max - i):
        print("*", end=" ")
    print()
    

print(f"-" * 10)

print(f"Tabel Perkalian 1 - 5")

for i in range(1, 6): # lakukan for loop sebanyak 5 kali
    for j in range(1, 6): # lakukan for loop sebanyak 5 kali
        print(f"{i} x {j} = {i * j}", end="\t") # menampilkan i x j = i * j
    print() # menampilkan baris baru
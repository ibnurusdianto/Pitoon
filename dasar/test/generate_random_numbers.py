import random 

print(f"===== GENERATE RANDOM NUMBERS =====")

while True:
    jumlah = int(input("Masukan jumlah angka : "))
    if jumlah > 0:
        break
    else:
        print("Jumlah harus lebih dari 0")

for i in range(jumlah):
    print(random.randint(1, 100))

print(f"===== TERIMA KASIH =====")

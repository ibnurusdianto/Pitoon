"""
Break statement python
"""

for i in range(10): # tampilkan number 1 - 9
    if i == 5: # jika i == 5 maka akan di break
        break
    print(i) # menampilkan i

print("selesai") # selesai

print(f"-" * 10) # menampilkan strip sebanyak 10 kali

angka_secure = 7
while True: # lakukan while loop 
    tebak_angka_secure = int(input("masukkan angka: ")) # masukkan angka
    if tebak_angka_secure == angka_secure: # jika tebak_angka_secure == angka_secure maka akan di break
        print("tebak angka secure benar")
        break
    else: # jika tebak_angka_secure != angka_secure maka akan di eksekusi
        print("tebak angka secure salah")

print("selesai") # selesai
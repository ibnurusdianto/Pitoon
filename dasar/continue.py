"""
Continue Statement Python 
"""


# versi menampilkan angka ganjil
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list_number: # tampilkan number 1 - 10
    if i % 2 == 0: # jika i % 2 == 0 maka akan di continue
        continue # continue akan mengabaikan baris kode setelahnya dan melanjutkan ke iterasi berikutnya
    print(i) # menampilkan i

print("selesai") # selesai

print(f"-" * 10) # menampilkan strip sebanyak 10 kali

# versi menampilkan angka genap
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list_number: # tampilkan number 1 - 10
    if i % 2 == 1: # jika i % 2 == 1 maka akan di continue
        continue # continue akan mengabaikan baris kode setelahnya dan melanjutkan ke iterasi berikutnya
    print(i) # menampilkan i

print("selesai") # selesai


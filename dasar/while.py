"""
While Loop
"""

number = 1 # mulai dari satu
while number <= 10: # selama numbernya kurang dari 10 maka akan di eksekusi
    print(number)
    number += 1  # di akhir tambahkan 1 ke number, jika tidak maka akan terjadi infinite loop

print("selesai") 

print(f"-" * 10)

# input sampai benar 
password = "" # deklarasikan password kosong 
while password != "12345": # lakukan while loop, jika password bukan 12345 maka akan di eksekusi
    password = input("masukkan password: ")
    if password == "12345": # jika password benar maka akan di eksekusi
        print("password benar")
    else: # jika password salah maka akan di eksekusi
        print("password salah")

print("selesai") # akhir dari while loop
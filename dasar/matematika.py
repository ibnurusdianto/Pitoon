"""
Matematika
"""
import math 

# matematika dasar
a = 10 
b = 7 

tambah = a + b 
kurang = a - b 
kali = a * b 
bagi = a / b 
modulus = a % b 
pangkat = a ** b 

print(f"tambah {tambah}") 
print(f"kurang {kurang}") 
print(f"kali {kali}") 
print(f"bagi {bagi}") 
print(f"modulus {modulus}") 
print(f"pangkat {pangkat}") 

print(f"===== Batas =====")

# matematika complex
kompleks = 2 + 3j 
print(f"kompleks {kompleks}") 
print(f"bagian real {kompleks.real}") 
print(f"bagian imajiner {kompleks.imag}") 


# matematika dengan menggunakan module math 
print(f"===== Batas =====")

angka = 10.5 
print(f"pembulatan ke atas {math.ceil(angka)}") # 11
print(f"pembulatan ke bawah {math.floor(angka)}") # 10
print(f"pembulatan terdekat {round(angka)}")  # 10
print(f"akar kuadrat dari {math.sqrt(64)}")
print(f"pangkat versi module math {math.pow(2, 3)}")
print(f"faktorial dari 5 adalah {math.factorial(5)}")
print(f"nilai pi {math.pi}")
print(f"nilai e {math.e}")
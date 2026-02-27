"""
Numbers Guessing Random 
"""

import random 

print(f"===== NUMBERS GUESSING RANDOM =====")

while True:
    number = int(input("Masukan angka : "))
    if number == random.randint(1, 100):
        print("Benar")
        break
    else:
        print("Salah")

print(f"===== TERIMA KASIH =====")
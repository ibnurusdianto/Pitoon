"""
User input adalah, sebuah fungsi yang digunakan untuk memasukan inputan pengguna

sedangkan error handling adalah sebuah teknik yang digunakan untuk 
menangani error yang terjadi pada program
"""

# user input dasar
nama = input("masukan nama anda : ")
print(f"nama anda adalah {nama}")

# user input dengan spesifikasi tipe data 
kakak = str(input("Masukan nama kakak anda : "))
usia_kakak = int(input("Masukan usia kakak anda : "))
print(f"nama kakak anda adalah {kakak}")
print(f"usia kakak anda adalah {usia_kakak}")

# contoh error handling try expect 
try:
    angka = int(input("masukan angka : "))
except ValueError:
    print("anda memasukan bukan angka")
else:
    print(f"Angka yang anda masukan adalah {angka}")

# part 2 contoh error handling try expect 
try:
    angka = int(input("masukan angka : "))
    print(f"Angka yang anda masukan adalah {angka}")
except ValueError:
    print("anda memasukan bukan angka")


# menghitung luas persegi panjang
print("menghitung luas persegi panjang")
try:
    panjang = int(input("masukan panjang : "))
    lebar = int(input("masukan lebar : "))
    if not panjang:
        raise ValueError("panjang tidak boleh kosong")
    if not lebar:
        raise ValueError("lebar tidak boleh kosong")
    if panjang < 0 or lebar < 0:
        raise ValueError("panjang dan lebar tidak boleh negatif")
    luas = panjang * lebar
    print(f"luas persegi panjang adalah {luas}")
except ValueError:
    print("anda memasukan bukan angka")


    

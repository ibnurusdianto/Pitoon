"""
Dalam tipe data memiliki beberapa jenis, yaitu:
1. String
2. Integer
3. Float
4. Boolean
5. List
6. Tuple
7. Dictionary

untuk mengecek apakah benar tipe data tersebut string atau bukan gunakan type

"""

# string 
nama = "ibnu"
print(type(nama))   

# integer 
usia = 23 
print(type(usia))   

# float 
nilai = 8.5
print(type(nilai)) 

# boolean 
benar = True 
print(type(benar))
salah = False 
print(type(salah))

# list 
hobi = ["membaca", "berenang", "bermain gitar"]
print(type(hobi))

# tuple 
buah = ("mangga", "pisang", "semangka")
print(type(buah))

# dictionary 
mahasiswa = {"nama": "ibnu", "usia": 23, "nilai": 8.5}
print(type(mahasiswa))

"""
ada tipe data lainnya 
"""

biner = 0b01010101
print(biner)
print(type(biner))

heksadesimal = 0xff
print(heksadesimal)
print(type(heksadesimal))

octal = 0o123
print(octal)
print(type(octal)) 
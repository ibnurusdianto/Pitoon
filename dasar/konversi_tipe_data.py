"""
dalam konversi tipe data ada beberapa cara, yaitu:
1. otomatis
2.  manual 
"""
# otomatis, yaitu int to float 
number = 10 
number2 = 10.5 
tambah = number + number2 
print(f"total jumlah {tambah}") 
print(f"jenis tipe data hasil pertambahan {type(tambah)}")  
print(f"jenis tipe data original {type(number)} dan {type(number2)}") 

# sedangkan manual, contoh str ke int dan sebaliknya 
number = "10"
number2 = 20 
tambah = int(number) + number2 
print(f"total jumlah {tambah}") 
print(f"jenis tipe data hasil pertambahan {type(tambah)}")  
print(f"jenis tipe data original {type(number)} dan {type(number2)}") 

# bisa juga kita melakukan konversi pada literals numbers, contoh biner to heda 
biner = "0b0101010101"
toInt = int(biner, 2) 
toHexa = hex(toInt) 
print(f"biner {biner} ke int {toInt} ke hexa {toHexa}") 

# atau cara cepat yaitu 
biner = 0b010101010101111 # namun dibacanya yaitu integer
toHexa = hex(biner) 
print(f"biner {biner} ke hexa {toHexa}") 

# dictionary ke dalam list 
data = {"nama": "budi", "umur": 20, "pekerjaan": "programmer"} 
listData = list(data) 
# gunakan .items() untuk mendapatkan key dan value 
listData2 = list(data.items()) 
print(f"dictionary {data} ke list versi keys saja {listData}") 
print(f"dictionary {data} ke list versi key dan value {listData2}") 

# list ke dalam tuple 
dataList = [1, 2, 3, 4, 5] 
tupleData = tuple(dataList) 
print(f"list {dataList} ke tuple {tupleData}") 

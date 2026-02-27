print(f"===== DATA SISWA =====") 

file = open("data_siswa.txt", "w")

while True:
    nama = str(input("Masukan nama (enter untuk selesai) : "))
    if nama == "":
        break
    
    nilai = int(input("Masukan nilai : "))
    
    file.write(f"{nama} : {nilai}\n")
    print(f"Data", nama, "berhasil ditambahkan")

file.close()
print(f"Berhasil menyimpan data")

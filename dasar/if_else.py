"""
Kondisi percabangan atau if else python 
"""

grade = "A"
numbers = 87 

if grade == "A" or numbers >= 90:
    print("Luar biasa")
elif grade == "B" or numbers >= 75:
    print("Bagus")
elif grade == "C" or numbers >= 60:
    print("Cukup")
else:
    print("Kurang")
    

grade = int(input('Enter your current grade: '))
prev_grade = int(input('Enter your previous grade: '))

if grade >= 90 and prev_grade >= 65:
    print("awesome")
if grade >= 90 and prev_grade < 65:
    print("awesome. you definitely working hard, right?")
elif grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

if (grade >= 65 and not prev_grade >= 65) or (not grade >= 65 and prev_grade >= 65):
    print("at least you passed one exam. good job!")
    

"""
Berikut contoh program yaitu menghitung jenis usia, dimana jika yang di inputkan
angka nol atau negatif maka akan ditolak, jika usia lebih dari 18 tahun berarti dewasa, jika usia
lebih dari 30 tahun berarti tua, yang terakhir berarti masih anak anak
"""

try:
    usia = int(input("Masukkan usia Anda: "))
    if usia <= 0:
        print("Usia tidak boleh negatif atau nol")
    elif usia > 18 and usia <= 30:
        print("Dewasa")
    elif usia > 30:
        print("Tua")
    else:
        print("Anak-anak")
except ValueError:
    print("Usia harus berupa angka")
"""
Literals Number
""" 

def biner_to_desimal(biner):
    desimal = 0
    for digit in biner:
        desimal = desimal * 2 + int(digit)
    return desimal

def desimal_to_biner(desimal):
    biner = ""
    while desimal > 0:
        biner = str(desimal % 2) + biner
        desimal = desimal // 2
    return biner

def desimal_to_hexadesimal(desimal):
    hexadesimal = ""
    while desimal > 0:
        hexadesimal = str(desimal % 16) + hexadesimal
        desimal = desimal // 16
    return hexadesimal

def hexadesimal_to_desimal(hexadesimal):
    desimal = 0
    for digit in hexadesimal:
        desimal = desimal * 16 + int(digit)
    return desimal

print(f"===== BINER TO DESIMAL =====")

biner = input("Masukan biner : ")
print("Desimal : ", biner_to_desimal(biner))

print(f"===== DESIMAL TO BINER =====")

desimal = int(input("Masukan desimal : "))
print("Biner : ", desimal_to_biner(desimal))

print(f"===== DESIMAL TO HEXADESIMAL =====")

desimal = int(input("Masukan desimal : "))
print("Hexadesimal : ", desimal_to_hexadesimal(desimal))

print(f"===== HEXADESIMAL TO DESIMAL =====")

hexadesimal = input("Masukan hexadesimal : ")
print("Desimal : ", hexadesimal_to_desimal(hexadesimal))
import random 

print(random.randint(1, 100)) # menampilkan angka random antara 1 sampai 100 

# bisa juga untuk string
options = ["heru", "ibnu", "tina", "aya"]
print(random.choice(options)) # menampilkan string random dari list
print(random.shuffle(options)) # mengacak urutan list
print(random.sample(options, 2)) # menampilkan 2 string random dari list    
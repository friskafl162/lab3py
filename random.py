from random import random

# meminta input jumlah bilangan acak yang lebih kecil dari 0.5
n = int(input("masukan nilai N: "))
count = 0

# loop untuk menghasilkan dan menampilkan bilangan acak yang kurang dari 0.5
while count < n:
    num = random()
    if num < 0.5:
        count += 1
        print(f"data ke—{count} =>{num}") 
print("selesai")
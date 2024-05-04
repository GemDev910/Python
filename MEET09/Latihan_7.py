Bilangan = int(input("Masukkan Bilangan: "))

while Bilangan % 2 == 0 or Bilangan < 20 or (Bilangan < 35 and Bilangan > 25) or Bilangan > 40:
    Bilangan = int(input("Masukkan Bilangan dalam rentang 10-15, 20-25, atau 35-40: "))

print("Benar")
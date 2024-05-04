# import random
# import string
# import os
# print("*"*21,"NILAI MEAN", "*"*21)
# Numbers = []
# Lanjut = True
# while Lanjut:
#     Numbers_Input = float(input("Masukkan Angka: "))
#     Numbers.append(Numbers_Input)
    
#     continue_input = input("lanjut(y/n)? ")
#     if continue_input.lower() != 'y':
#         Lanjut = False
# if Lanjut == False :
#     TotalNumbers = sum(Numbers)
#     Hasil = TotalNumbers/len(Numbers)
#     Hasil = round(Hasil, 2)
# print(Hasil)




print("*"*21, "NILAI MEAN", "*"*21)

def mean(*args, **kwargs):
    numbers = []
    lanjut = True
    while lanjut:
        number_input = int(input("Masukkan Angka: "))  # Menggunakan float() agar bisa menerima angka desimal
        numbers.append(number_input)
        
        continue_input = input("Lanjut (y/n)? ")
        if continue_input.lower() != 'y':
            lanjut = False

    total_numbers = sum(numbers)
    hasil = total_numbers / len(numbers)
    hasil = round(hasil, 2)  
    return hasil, numbers

rata_rata, list_number = mean()

print(f"Hasil mean dari data {list_number} = {rata_rata}")
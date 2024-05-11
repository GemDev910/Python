import Fisika
import time
def batas():
    print("-"*15)

waktu_awal = time.time()

print( f"Massa Jenis = { Fisika.MassaJenis.MassaJenis( 10, 2 )}")
print( f"Massa = { Fisika.MassaJenis.Massa( 10, 2 )}")
print( f"Volume = { Fisika.MassaJenis.Volume( 10, 2 )}")

waktu_akhir = time.time()
print( f"Waktu Yang Dibutuhkan : { waktu_akhir - waktu_awal }")

batas()
print( f"Usaha = { Fisika.U( 12, 3 ) }")
print( f"Gaya = { Fisika.G( 6, 2 ) } ")
print( f"Jarak = { Fisika.J( 0,3 ) } ")

batas()

print( f"Hasil Energi Potensial : { Fisika.Ep(4 , 7 , 4)}")
print( f"Hasil Energi Kinetik : { Fisika.Ep(4 , 7 , 4)}")

batas()

Diskon10 = Fisika.JL(10)
Diskon20 = Fisika.JL(20)

print(f"Diskon 10% = {Diskon10(10000)}")
print(f"Diskon 20% = {Diskon10(10000)}")
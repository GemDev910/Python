import Fisika
import time
def batas():
    print("-"*15)

waktu_awal = time.time()

print( f"Massa Jenis = { Fisika.MassaJenis.MassaJenis( 10, 2 )}")
print( f"Massa = { Fisika.MassaJenis.Massa( 10, 2 )}")
print( f"Volume = { Fisika.MassaJenis.Volume( 10, 2 )}")

waktu_akhir = time.time()
print( f" waktu yang dibutuhkan : { waktu_akhir - waktu_awal }")

batas()
print( f"usaha = { Fisika.U( 12, 3 ) }")
print( f"Gaya = { Fisika.G( 6, 2 ) } ")
print( f"Jarak = { Fisika.J( 0.3 ) } ")

batas()

print( f" Hasil Energi Potensial : { Fisika.Ep(4 , 7 , 4)}")
print(" \t TIKET BUS \t ")
print("_"*30)

print("Kode Kota :")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuk Linggau")
kota = int(input("Pilihan Kota (1/2/3) \t: "))

print("_"*30)
print("Kode Kelas :")
print("1. Ekonomi")
print("2. Bisnis")
print("3. Eksekutif")
kelas = int(input("Pilihan Kelas (1/2/3) \t: "))
jmlh_tiket = int(input("Jumlah Tiket \t: "))

Kode_promo = ""  # Initialize Kode_promo variable outside conditions

if kota == 2 and kelas == 1:
    Kode_promo = str(input("Masukkan kode promo : ").lower())
    
elif kota == 3 and kelas == 3:
    Kode_promo = str(input("Masukkan kode promo : ").lower())

print("_"*30)

if kota == 1 and kelas == 1:
    harga = 1000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 
elif kota == 1 and kelas == 2:
    harga = 4000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 
elif kota == 1 and kelas == 3:
    harga = 7000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 

if kota == 2 and kelas == 1:
    harga = 2000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 
elif kota == 2 and kelas == 2:
    harga = 5000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 
elif kota == 2 and kelas == 3:
    harga = 8000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 

if kota == 3 and kelas == 1:
    harga = 3000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 
elif kota == 3 and kelas == 2:
    harga = 6000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 
elif kota == 3 and kelas == 3:
    harga = 9000000
    subtotal = harga * jmlh_tiket
    print(f"Harga Tiket : Rp. {harga}")
    print(f"Subtotal : Rp. {subtotal}") 

if Kode_promo == "igs":
    diskon = 0.1 * subtotal
    print(f"Diskon : Rp. {diskon:>0.0f}")
else:
    diskon = 0  
    print(f"Diskon : Rp. {diskon:>0.0f}")

total = subtotal - diskon
print(f"Total : Rp. {total:>0.0f}")

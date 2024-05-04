# print("\t NOTA PENJUALAN - TOKO XYX \t >>")
# print("-"*42)
# nama_barang = input("Nama Barang\t: ")
# harga_barang = int(input("Harga Barang\t: "))
# Jumlah_Beli = int(input("Jumlah Beli\t: "))

# subTotal = harga_barang * Jumlah_Beli
# print(f"Sub Total\t:Rp. {subTotal:>20}")

# diskon = 0.2 * subTotal
# print(f"Diskon(20%)\t:Rp. {diskon:>20.0f}")

# total = subTotal-diskon
# print(f"Total Bayar\t:Rp. {total:>20.0f}")


# Besar_Bayar = int(input("Besar Bayar\t:Rp.                  "))

# print("-"*40)

# Kembalian = Besar_Bayar-total
# print(f"Kembalian\t:Rp. {Kembalian:>20.0f}")
# print("Jumlah Kembalian\t:              ")

# Fifty_Thousand= Kembalian // 50000
# print(f"Rp. 50000\t: {Fifty_Thousand:>20.0f}")
# Fifties_Thousand= Kembalian % 50000

# Twenty_Thousand= Fifties_Thousand // 20000
# print(f"Rp. 20000\t: {Twenty_Thousand:>20.0f}")
# Twenties_Thousand= Fifties_Thousand % 20000

# Ten_Thousand= Twenties_Thousand // 10000
# print(f"Rp. 10000\t: {Ten_Thousand:>20.0f}")
# Tens_Thousand= Twenties_Thousand % 10000

# Five_Thousand= Tens_Thousand // 5000
# print(f"Rp. 5000\t: {Five_Thousand:>20.0f}")
# Fives_Thousand= Tens_Thousand % 5000

# Two_Thousand= Fives_Thousand // 2000
# print(f"Rp. 2000\t: {Two_Thousand:>20.0f}")
# Twos_Thousand= Five_Thousand % 2000

# One_Thousand= Twos_Thousand // 1000
# print(f"Rp. 1000\t: {One_Thousand:>20.0f}")
# Ones_Thousand= Twos_Thousand % 1000

# Five_Hundred= Ones_Thousand // 500
# print(f"Rp. 500\t: {Five_Hundred:>20.0f}")
# Fives_Hundred= Ones_Thousand % 500

# Two_Hundred= Five_Hundred // 200
# print(f"Rp. 200\t: {Two_Hundred:>20.0f}")
# Twos_Hundred= Fives_Hundred % 200

# One_Hundred= Two_Hundred // 100
# print(f"Rp. 100\t: {One_Hundred:>20.0f}")
# Ones_Hundred= Twos_Hundred % 100

print("<< \t NOTA PENJUALAN - TOKO XYZ \t >>")
print("-"*42)

nama_barang = input("Nama barang\t: ")
harga_barang = int(input("Harga barang \t: "))
jumlah_beli = int(input("Jumlah beli\t: "))
subTotal = harga_barang * jumlah_beli
print(f"subTotal\t:Rp. {subTotal:>30,.0f}")

diskon = 0.2 * subTotal
print(f"diskon\t\t:Rp. {diskon:>30,.0f}")

total = subTotal - diskon
print(f"total\t\t:Rp. {total:>30,.0f}")

Besar_bayar = int(input("Total bayaran anda\t:Rp."))
print(f"Besar bayar\t:Rp. {Besar_bayar:>30,.0f}")

print("-"*42)
Kembalian = Besar_bayar - total
print(f"Kembalian\t:Rp. {Kembalian:>30,.0f}")

print("Rincian Kembalian:")
Changes_50 = Kembalian // 50000
Changes1 = Kembalian % 50000
print(f"Rp 50.000\t\t: {Changes_50:>30,.0f} lembar")

Changes_20 = Changes1 // 20000
Changes2= Changes1 % 20000
print(f"Rp 20.000\t\t: {Changes_20:>30,.0f} lembar")

Changes_10 = Changes2// 10000
Changes3 = Changes2% 10000
print(f"Rp 10.000\t\t: {Changes_10:>30,.0f} lembar")

Changes_5 = Changes3 // 5000
Changes4 = Changes3 % 5000
print(f"Rp 5.000\t\t: {Changes_5:>30,.0f} lembar")

Changes_2 = Changes4 // 2000
Changes5 = Changes4 % 2000
print(f"Rp 2.000\t\t: {Changes_2:>30,.0f} lembar")

Changes_1 = Changes5 // 1000
print(f"Rp 1.000\t\t: {Changes_1:>30,.0f} lembar")
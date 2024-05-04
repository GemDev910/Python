print("<<< \t\t PENJUALAN \t\t >>>")

harga = int(input("Masukkan harga \t\t: "))
qty = int(input("Masukkan jumlah beli \t: "))

subTotal = harga * qty
if qty >= 12:
    diskon = 0.20 * subTotal
else:
    diskon = 0

Total = subTotal - diskon
print(f"Subtotal\t\t: Rp. {subTotal:>20.0f}")
print(f"Diskon\t\t\t: Rp. {diskon:>20.0f}")
print(f"Total\t\t\t: Rp. {Total:>20.0f}")
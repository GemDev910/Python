from datetime import date as dt

print(f"<< \t\t UMUR \t\t >>")
print("-"*25)
print("Masukkan Tanggal, Bulan, Tahun")
print("\n")
tanggal = int(input("Tanggal \t\t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tgl_lahir = dt( tahun, bulan, tanggal)
today = dt.today()
print(f"Tanggal Lahir \t\t: {tgl_lahir} (Days : {tgl_lahir.day})")
print(f"Tanggal hari Ini \t: {today}")
selisih_tgl = today - tgl_lahir
print(f"Selisih Tanggal : {selisih_tgl.days}")

usia_tahun = selisih_tgl.days // 365   
usia_sisa_bulan = (selisih_tgl.days % 365) // 30
usia_sisa_hari = (selisih_tgl.days % 365 % 30) // 1
print(f"Umur Anda {usia_tahun} Tahun Dan {usia_sisa_bulan} Bulan {usia_sisa_hari} Hari")



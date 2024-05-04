# 3 Cara Untuk Membuat Format String :
# 1. Format (%)
# 2. Format String
# 3. f.string

umur = 15 # Tp : Integer (I/D)
nama = "Noir" # Tp : String (s)
ukuran_sepatu = 42 # Tp: Float (f)
# Dengan Format %
print(" Hei Nama Saya %s Umur Saya %d Dan memiliki Ukuran Sepatu %0.2f " %( nama, umur, ukuran_sepatu))

print("-"*15, ">Format String")
print("1.Array : Hei Nama Saya {0} Umur Saya {1} Dan Memilih Ukuran Sepatu {2}" .format( nama, umur, ukuran_sepatu))

print("-"*15, ">Format Shortened")
print("2.Array : Hei Nama Saya {nm} Umur Saya {u} Dan Memilih Ukuran Sepatu {us}" .format( nm=nama, u=umur, us=ukuran_sepatu))

print("-"*15, ">f.String")
print(f"Dengan f.String : Hei Nama Saya {nama} Umur Saya {umur} Dan Ukuran Sepatu {ukuran_sepatu} ")

print("-"*15, ">Allignment Dengan Format String")
print("name : [ {0} ]" .format(nama))
print("name : [ {} ]" .format(nama))
print("name : [ {:<15} ]" .format(nama))
print("name : [ {:>15} ]" .format(nama))
print("name : [ {:^15} ]" .format(nama))

print("-"*15, ">Allignment Dengan F.String")
print( f"name : [ {nama} ]" )
print( f"name : [ {nama:<15} ]" )
print( f"name : [ {nama:>15} ]" )
print( f"name : [ {nama:^15} ]" )

print("-"*15, ">Allignment Dengan %")
print("name : [ {0} ]" .format(nama))
print("name : [ {} ]" .format(nama))
print("name : [ {:<15} ]" .format(nama))
print("name : [ {:>15} ]" .format(nama))
print("name : [ {:^15} ]" .format(nama))




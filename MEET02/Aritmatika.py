'''
Aritmatika Python :
1. + (Penjumlahan)
2. - (Pengurangan)
3. * (Perkalian)
4. / (Pembagian)
5. ** (Pangkat)
6. % (Modulus)
7. // (Hasil Bagi)
'''

a = 8
b = 4

print("-"*1, "Penjumlahan","-"*1)
Hasil = a + b
print( a, "+",  b ,  "=", Hasil)
print( a, "+",  b ,  "=", a + b)

print("-"*1, "Pengurangan","-"*1)
Hasil = a - b
print( a, "-",  b ,  "=", Hasil)
print( a, "-",  b ,  "=", a - b)

print("-"*1, "Perkalian","-"*1)
Hasil = a * b
print( a, "*",  b ,  "=", Hasil)
print( a, "*",  b ,  "=", a * b)

print("-"*1, "Pembagian","-"*1)
Hasil = a / b
print( a, "/",  b ,  "=", Hasil)
print( a, "/",  b ,  "=", a / b)

print("-"*1, "Pangkat","-"*1)
Hasil = a ** b
print( a, "Pangkat",  b ,  "=", Hasil)
print( a, "Pangkat",  b ,  "=", a ** b)

print("-"*1, "Modulus","-"*1)
Hasil = a % b
print( a, "%",  b ,  "=", Hasil)
print( a, "%",  b ,  "=", a % b)

print("-"*1, "Hasil Bagi","-"*1)
Hasil = a // b
print( a, "//",  b ,  "=", Hasil)
print( a, "//",  b ,  "=", a // b)

'''
Prioritas Operasi Di Python
1. ()
2. **
3. * / % //
4. +-
'''
x = 8
y = 10
z = 12
print("-"*1, "Operasi Arimkatika 1","-"*1)
Hasil = x*(y-z)
print("x","*","(y-z)","=", Hasil)

print("-"*1, "Operasi Arimkatika 2","-"*1)
Hasil = (x+y)//(z-x)**x
print("(x+y)//(z-x)**x","=", Hasil)
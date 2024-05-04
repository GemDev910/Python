'''
Operator Perbandingan :
1. >
2. <
3. >=
4. <=
5. ==
6. !=
'''

a = 50
b = 100

print("-"*15, ">")
hasil = a > b
print(a,">",b,"=",hasil)
hasil = a > 2
print(a,">",2,"=",hasil)

print("-"*15, "<")
hasil = a < b
print(a,"<",b,"=",hasil)
hasil = a < 2
print(a,"<",2,"=",hasil)

print("-"*15, ">=")
hasil = a >= b
print(a,">=",b,"=",hasil)
hasil = a >= 50
print(a,">=",50,"=",hasil)

print("-"*15, "<=")
hasil = a <= b
print(a,"<=",b,"=",hasil)
hasil = a <= 50
print(a,"<=",50,"=",hasil)

print("-"*15, "==")
hasil = a == b
print(a,"==",b,"=",hasil)
hasil = a == 50
print(a,"==",50,"=",hasil)

print("-"*15, "!=")
hasil = a != b
print(a,"!=",b,"=",hasil)
hasil = a != 50
print(a,"!=",50,"=",hasil)

import aritmatika
from mtk.rumusMtk import tambahan, kalian
import fisika

def batas():
    print( "-"*15)

resultPlus = aritmatika.plus( 9,3 )
resultMin = aritmatika.min( 9,3 )
resultKali = aritmatika.kali( 9,3 )
resultBagi = aritmatika.bagi( 9,3 )

print (f" 9 + 3 = {resultPlus} ")
print (f" 9 - 3 = {resultMin} ")
print (f" 9 * 3 = {resultKali} ")
print (f" 9 / 3 = {resultBagi} ")

batas()

resultTambahan = tambahan( 4, 5, 2, 1, 7 )
print(f"1. Hasil Tambahan = {resultTambahan}")
resultKalian = kalian( 4, 5, 2, 1, 7 )
print(f"1. Hasil Tambahan = {resultTambahan}")
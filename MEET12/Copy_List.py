data1 = [1,2,3,4]
data2= ["a","b","c"]
datalist1 = data1
print(f"Data1 = {data1}")
print(f"datalist1 = {datalist1}")
data1[-1]= 100
print(f"Data1 UPDATED= {data1}")
print(f"datalist1 UPDATED= {datalist1}")
print(f"Memory Address data1 {hex(id(data1))}")
print(f"Memory Address datalist1 {hex(id(datalist1))}")

print("-"*15)
datalist2 = data2.copy()
print(f"Memory Address data2 {hex(id(data2))}")
print(f"Memory Address datalist2 {hex(id(datalist2))}")
data2[0]= "xyz"
print(f"Data2 UPDATED= {data2}")
print(f"datalist2 UPDATED= {datalist2}")


print("-"*15, "Nested List")
data1 = ["I","G","S"]
data2 = [10,11,12]



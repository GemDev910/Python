data = "Ignatius Global School"

#menghitung jumlah str
print(f"Jumlah Str DI Data: {len(data)}")

#in - not in, mengetahui str
print(f"Apakah ada 'i' di str : {'i' in data}")
print(f"Apakah ada 'z' di str : {'z' in data}")
print(f" 'z' not in data ? : {'z' not in data}")
print(f" 'i' not in data ? : {'i' not in data}")

# min / max pada str
print(f"min pada data : {min ('abcdgazgh')}")
print(f"max pada data : {max (data)}")

#menghitung karakter str :
print(f" 'o' pada data : { data.count('o')}")

data1 = "ini huruf kecil"
data2 = "INI HURUF BESAR"
print(f" data1 : { data.upper()}")
print(f" data2 : { data.lower()}")
data3 = "123123"
print (f" data1 is alpha: {data1.isalpha()}")
print (f" data3 is alpha: {data3.isalpha()}")

#index in str
print(f" data ke-0 : {data[0]}")
print(f" data ke-2 : {data[2]}")
print(f" data ke-0,8 : {data[0:8]}")
print(f" data ke-0,8,2 : {data[0:8:2]}")
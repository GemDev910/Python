#FromKeys : Dict
data = dict.fromkeys(range (5), "oke")
print(f"data = {data}")

print("-"*20)
data = {
    "Siswa" : "",
    "Kelas" : "",
    "Jurusan" : "",
    
}
datas = dict.fromkeys(data.keys())
data["siswa"] = input("Siswa = ")
data["kelas"] = input("Kelas = ")
data["jurusan"] = input("Jurusan = ")
NewData = {"siswa01" : data}
print(f"Newdata = {NewData}")

print("-"*20)
import random
import string
keys_1 = random.randint(1,10)
print(f"Keys_1 = {keys_1}")
keys_2 = random.choice("ABCDEF")
print(f"Keys_2 = {keys_2}")
print(f"A - Z = {string.ascii_uppercase}")
keyFinal = "".join()


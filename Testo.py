# import random
# import string
# import os
# hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
# mata_pelajaran = {}
# Lanjut = True
# while Lanjut:
#     print("*"*21,"-DAFTAR MAPEL", "*"*21)
#     mapel = input("Mapel  : ")
#     guru = input("guru  : ")
#     hari_kelas = input("hari  : ")
#     jam_kelas = input("jam  : ")
#     ruangan = input("ruangan  : ")
#     id_mapel = ''.join(random.choices(string.ascii_uppercase, k=3)) + ''.join(random.choices(string.digits, k=3))
#     mata_pelajaran[id_mapel] = {"Mapel": mapel, "guru": guru, "hari": hari_kelas, "jam": jam_kelas, "ruangan": ruangan}
#     continue_input = input("lanjut(y/t)? ")
#     if continue_input.lower() != 'y':
#         Lanjut = False
# os.system("cls" if os.name == "nt" else "clear")
# print("*"*21,"-DAFTAR MAPEL", "*"*21)
# for id_mapel, info in mata_pelajaran.items():
#     print("Mapel  :", info['Mapel'])
#     print("guru  :", info['guru'])
#     print("hari  :", info['hari'])
#     print("jam  :", info['jam'])
#     print("ruangan  :", info['ruangan'])
#     print("*"*110)
# print("ID\t\tMAPEL\t\t\tGURU\t\tHARI\t\tJAM\t\tRUANGAN")
# print("*"*110)
# for id_mapel, info in mata_pelajaran.items():
#     print(f"{id_mapel}\t\t{info['Mapel']:20}\t{info['guru']:15}\t{info['hari']:10}\t{info['jam']:10}\t{info['ruangan']:10}")


def mean(*args, **kwargs):
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        data = args[0]
    else:
        data = args
    weights = kwargs.get('weights', None)
    if weights is None:
        return sum(data) / len(data)
    else:
        if len(data) != len(weights):
            raise ValueError("Panjang data dan weights harus sama")
        weighted_sum = sum(x * w for x, w in zip(data, weights))
        total_weight = sum(weights)
        return weighted_sum / total_weight


data = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]

print("Mean:", mean(*data))
print("Weighted Mean:", mean(*data, weights=weights))
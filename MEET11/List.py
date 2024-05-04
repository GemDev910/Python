# List:
# 1.Number
# 2. Karakter/ String
# 3. Bool
list_num = [1, 2, 3, 4, 10]
print(f"Data List Angka : {list_num}")
list_str = ["q", "w", "e", "r", "t", "y"]
print(f"Data List Str : {list_str}")
list_bool = [True, False, False, True]
print(f"Data List Bool : {list_bool}")

list_mix = [
    1,
    2,
    True,
    "ABC"
]
print(f"Data List Mix : {list_mix}")
print("-"*10, "List : LOOP-For")
data_loop = [i for i in range(1, 10, 2)]
print(f"Data List loop : {data_loop}")
data_1 = [i for i in range(1, 10)if i%2]
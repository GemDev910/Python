#list
dataList = [1,2,3,4]
dataTuple = ("a","b","c")
dataSet= {"x","y","z"}
print(f"List = {dataList}")
print(f"Tuple = {dataTuple}")
print(f"Set  = {dataSet }")
print("-"* 15)
print(f"Data List Ke 0 = {dataList[0]}")
print(f"Data Tuple Ke 0 = {dataTuple[0]}")
#print(f"Data Set Ke 0 = {dataSet[0]}")
print("-"* 15)
dataList.insert(0,"Awal")
print(f"List = {dataList}")
dataSet.add("Igs")
print(f"List = {dataSet}")
#dataTuple.add("Oke") # tdk bisa
print("-"* 15) #remove
dataList.remove("Awal")
print(f"List = {dataList}")
dataSet.remove("Igs")
print(f"List = {dataSet}")


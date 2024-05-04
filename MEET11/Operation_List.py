data_list1 = ["Ignatius","Global","School"]
print(f"Data_List Ke-0 : {data_list1[0]}")
print(f"Data_List Ke-1 : {data_list1[1]}")
print(f"Data_List Ke-2 : {data_list1[2]}")
print(f"Data_List Ke -2 : {data_list1[-2]}")
print(f"Data_List Ke -1 : {data_list1[-1]}")
print(f"Data_List Ke -3 : {data_list1[-3]}")
print("-"*10, "Bagian/irisan -Item list")
data_list2= [1,2,3,4, "a","b", True]
print(f"Data List2 [0:3] : {data_list2[0:3]}")
print(f"Data List2 [-2:1] : {data_list2[-2:1]}")
print(f"Data List2 [1:] : {data_list2[1:]}")
print(f"Data List2 [:-2] : {data_list2[:-2]}")

print("-"*10, " -Join list")    

data1 = [1,2,3,4]
data2 = ["a","b","c","d"]
print(f"Data 1 + Data 2 {data1 + data2}")
data1.extend(data2)
print(f"Data 1 = {data1}")


print("-"*10, "Len-")  
print(f"Jumlah Item Data1 = {len(data1)}")

print("-"*10, "Repetition")  
data3 = ["x","y","z"]*3
print(f"Data 3= {(data3)}")

print("-"*10, "Membership")
if "x" in data3:
    print("True")
else:
    print("False")
print("-"*10, "Iterasi")
for i in data_list1:
    print(f"Data = {i}")
    
print("-"*10, "Add -Item")
data_list1.insert(0,"SMA")
print(f"Data_List1 - Insert : {data_list1}")
data_list1.append("Terbaik")
print(f"Data_List1 - Append : {data_list1}")

print("-"*10, "Update -Item")
data_list1[-1] = "Oke"
print(f"Data_List1 - Update : {data_list1}")

print("-"*10, "Delete -Item")
data_list1.pop()
print(f"Data_List1 - DELETE.pop : {data_list1}")
data_list1.remove("SMA")
print(f"Data_List1 - DELETE.remove : {data_list1}")
del data_list1[-1]
print(f"Data_List1 - DELETE.del: {data_list1}")

print("-"*10, "INDEX -Item")
data5 = [1,1,6,2,3]
print(f" data5: 2 = {data5.index(2)}")

print("-"*10, "Count -Item")
print(f" Jumlah Item(1) di data5 = {data5.count(1)}")

print("-"*10, "max-min -Item")
print(f" max data5= {max(data5)} min data5= {min(data5)}")

print("-"*10, "Sorting -Item")
data5.sort()
print(f"Sort = {data5}")
data5.reverse()
print(f"Reverse = {data5}")


    

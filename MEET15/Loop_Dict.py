dataDict = {
    "Plb" : "Palembang",
    "Lnd" : "London",
    "Prs" : "Paris" ,
    "Milan" : "Italia"
    
}
for i in dataDict:
    print(f"i = {i}")
    
print(f"-"*15,"KEYS")
print(f"Keys In Datadict = {dataDict.keys()}")
for z in dataDict.keys():
    print(f"z = {z}")
    
print(f"-"*15,"VALUE")
print(f"VALUES In Datadict = {dataDict.values()}")
for x in dataDict.values():
    print(f"x = {x}")
    
print(f"-"*15,"Itemw")
print(f"Items In Datadict = {dataDict.items()}")
for K, V in dataDict.items():
    print(f"{K} = {V}")
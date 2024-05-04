#pass
print("-","- Pass")
for i in range(5):
    print( f"{i}")
    if i == 3 :
        pass
print("-","*20")
for i in range (7):
    if i == 5:
        pass
    else:
        print(f"{i}")
print("-","*20")
try:
    a = int (input ("A = "))
    b = int (input ("B = "))
    print(f"{a} + {b} = {a+b}")
except:
    pass

print("-"*15,"- Break")
for i in range(10):
    if i == 3 :
        break
    else:
        print( f"{i}")
        
print("-"*15,"- Continue")
for i in range(10):
    if i == 3 :
        continue
    else:
        print( f"{i}")
print("*")
print("**")
print("*")
print("**")
print("***")
print("**")

print ( " - for"*10)
for i in range(10):
    print( "+"*i)

print (" - while"*10)
i = 0
while i < 10:
    i += 1
    print( f"{i}"* i)

print ( "ganjil-"*10)
i = 0
while True:
    if i == 20:
        break
    elif i % 2:
        print( f"+" * i)
    i += 1

print ( ">"*10)
i = 0
count = 20
space = 20
while True:
    if i == count:
        break
    elif i & 2 :
        print(f"")



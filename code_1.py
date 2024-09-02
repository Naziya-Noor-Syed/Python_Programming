data = input("data:")
l = data.split(",")
print("list:", l)
i = int(input("index: "))
if(i>=0 and i<len(l) or i>-len(l) and i<=0):
    print("element:",l[i])
else:
    print("invalid")
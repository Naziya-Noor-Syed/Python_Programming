"""Print the elements of the following list using a loop
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for ele in num:
    print(ele)
"""
"""
# Search for a number x in this tuple using loop:
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter a num:"))
for ele in num:
    if(ele == x):
        print("Found")
    else:
        print("not found")
        """

str = "Syedfamily"

for ele in str:
    if(ele == "m"):
        print("Found m")
        break
    print(ele)

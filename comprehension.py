# ls = []
# for i in range(1, 100):
#     if i%3 == 0:
#         ls.append(i)
    
# print(ls)

ls = [i for i in range(1, 100) if i%3 == 0]

print(ls)
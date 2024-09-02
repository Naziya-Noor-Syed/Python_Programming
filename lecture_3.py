#list of elements
"""a built in data type that stores set of values"""
"""
marks = [25.5, 65.1, 85.4, 25.6, 94.5]
print(marks)
print(len(marks)) #length
print(marks[3]) #indexing

"""
"""
Student = ["Naseera", 21, "Anantapur"]
Student[0] = "Naziya"
print(Student)

"""


#list of slicing
"""
marks = [54, 63, 98, 45, 21]
print(marks[1:3])
print(marks[:3])
print(marks[1:])
print(marks[-4:-2])

"""

#list of method
"""
list = [2, 1, 3]
list.append(4) # adding one element at the end
print("added an element:", list)
list.sort() #sorting to ascending order
print("Ascending order:" , list)
list.sort(reverse=True) #sorting to descending order
print("Descending order:", list)
list.reverse() # reverse list
print("reverse list:", list)
list.insert(1,5) #inserted element
print("inserted element:", list)

"""

#list of method

list = [2, 1, 3, 1]
list.pop(3)
print(list)
Students = {
    "name" : "Naziya",
    "subjects" :{
        "Physics" : 24,
        "Chemistry" : 56,
        "Maths" :65
    }

}

new_dict = Students.update({"name" : "naseera", "age" : 24})
print(list(Students))






"""
#methods

print(Students.keys()) # returns keys
print(Students.values()) #return values
print(Students.items()) # returns both keys and values
print(list(Students.items())) 
print(Students.get("name")) # return key according to value
print(Students.get("name2")) # return the none values

"""




#nested dict
""" print(Students["subjects"]["Chemistry"]) """
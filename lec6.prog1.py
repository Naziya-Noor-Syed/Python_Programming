#WAF to print the length of a list. ( list is the parameter)
cities = ["Delhi", "Atp", "Bangalore"]
def length_list(list):
    print(len(list))

length_list(cities)
# WAF to print the elements of a list in a single line. ( list is the parameter)
def list(lists):
    for item in lists:
        print(item, end=" ")

list(cities)
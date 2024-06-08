tuple1 = (1, 2, 3, "String", False, [0, 2, 4], (False, True))
#print(tuple1)

#accessing tuple elements
# print(tuple1[-1][-1])
# print(tuple1[::-1])
# print(tuple1[:4])

#creation of a tuple using constructor
# tuple2 = tuple("A string that will be turned into a tuple...")
# print(tuple2)

list1 = [3, 4, 5, True, False, True, 3, 5, 6, 7, 3, "string", "string", (1, 2, 3)]

#conversion between a tuple and a list
tuple3 = tuple(list1)
print("Conversion of a list into a tuple with tuple(): ", tuple3)

list2 = list(tuple3)
print("Conversion of a tuple back into a list with list(): ", list2)

#indexing works as in the case of a list
print(tuple3.index(True, 4))

#counting elements inside a tuple
print(tuple3.count(True))

#counting all elements in a tuple
print("The amount of all elements inside a tuple is: ", len(tuple3)) #13 elemnts

#checking unique values
uniqueValues = set(tuple3)
print(uniqueValues)
print("There are " + str(len(uniqueValues)) + " unique, non-duplicated values.")

single = ("My first", "My second", "My third")
single2 = (1, 2, 3) #hashable collection leads to optimisation of code execution: memory saving

print(single == single2)
print(single is single2)
print(id(single))
print(id(single2))

#tuple unpacking
var1, *var2 = single
print(var1)
print(var2)
#print(var3)

#list unpacking
list1 = ["list1", 'list2', "list3"]
var4, *var5 = list1
print(var5)




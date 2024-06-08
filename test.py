# MainList=[['x11','x12','x13'],
#           ['x21','x22','x23'],
#           ['x31','x32','x33'],
#           ['x41','x42','x43']]
# print (MainList[0:4])
# print (MainList[0:[2]])
# print (MainList[:4][:2][0:2][0:2])
# # print (MainList[0:3][0:2][0])
# # print (MainList[0:3][0][0])

# import numpy as np

# myList = np.array(MainList)
# #print (myList)
# # twoColumns=myList[0:2,0:2]
# # print(twoColumns)

# tuple1 = (1, 2, 3, "String", False, [0, 2, 4], (False, True))
# list1 = [3, 4, 5, True, False, True, 3, 5, 6, 7, 3, "string", "string", (1, 2, 3)]
# tuple3=tuple(list1)
# print(list1)
# print(tuple3)

# test1=[1,2,3]
# print(test1)
# test1[0:2]=[0,9]
# print(test1)
# tuple2=tuple(test1)
# list2=list(test1)
# print('tuple',tuple2)
# print('list',list2)
# list2[0]=[6,5]
# print(list2)
# tuple3=tuple2.index(3,2)
# print(tuple3)

# list1 = [3, 4, 5, True, False, True, 3, 5, 6, 7, 3, "string", "string", (1, 2, 3)]
# tuple3 = tuple(list1)
# # print(tuple3.index(True, 4))
# # print(tuple3.count(True))
# # print("The amount of all elements inside a tuple is: ", len(tuple3))
# uniqueValues = set(tuple3)
# print(uniqueValues)
# print("There are " + str(len(uniqueValues)) + " unique, non-duplicated values.")

# single = ("My first", "My second", "My third")
# single2 = (1, 2, 3) #hashable collection leads to optimisation of code execution: memory saving

# print(single == single2)
# print(single is single2)
# print(id(single))
# print(id(single2))

# #tuple unpacking
# var1, *var2 = single
# print(var1)
# print(var2)
#print(var3)

# #list unpacking
# list1 = ["list1", 'list2', "list3"]
# var4, *var5 = list1
# print(var5)


#sentence=' lib jocks quiz nymph to vex dwarf.'

# def is_pangram (sentence1):
#     sentence2=sentence1.lowercase()
#     setAlphabet='abcdefghijklmnopqrstuvwxyz'
#     for x in setAlphabet:
#         for y in sentence1:
#             if x != y:
#                 print('False')
#         else:
#                 print('True')
# c1=is_pangram(sentence)
# print()

# def is_pangram (sentence1):
#     setAlphabet='abcdefghijklmnopqrstuvwxyz'
#     letter=0
#     for j in setAlphabet:
#         letter += 1

#         if(letter not in sentence1):
#             return False
#         else:
#             return True
# result=is_pangram(sentence)
# print(result)

# setAlphabet='abcdefghijklmnopqrstuvwxyz'

# def is_pangram (sentence1):
#     setAlphabet='abcdefghijklmnopqrstuvwxyz'
#     for c in setAlphabet:
#              for 
#              if (c in (for x in sentence1)):
#                   return True
#              else:
#                 return False
# sentence=' gli jocks quiz nymph to vex dwarf.'
# x2=is_pangram(sentence)
# print(x2)


#setAlphabet='abcdefghijklmnopqrstuvwxyz'

# sentence111=sentence1.isalpha()
# sentence11=sorted(sentence111)
# print(sentence11)

# def is_pangram (sentence):
#     Alphabet='abcdefghijklmnopqrstvwxyz'
#     psentence= sentence.lower()
#     setSentence=set(psentence)
#     set2Sentence=sorted(setSentence)
#     setAlphabet=set(Alphabet)
#     if setAlphabet == setAlphabet.intersection(set2Sentence):
#         return True
#     else:
#         return False

#     # for x in setAlphabet:
#     #     for y in psentence:
#     #         if (x not in psentence):
#     #             return False 
#     #         else:
#     #             return True
# z1= is_pangram(sentence1)
# z2= is_pangram(sentence2)
# z3= is_pangram(sentence3)
# z4= is_pangram(sentence4)
# z5= is_pangram(sentence5)
# z6= is_pangram(sentence6)
# z7= is_pangram(sentence7)
# z8=is_pangram(sentence8)
# print(z1,z2,z3,z4,z5,z6,z7,z8,sep='\n')


def is_pangram (sentence):
    setAlphabet='abcdefghijklmnopqrstuvwxyz'
    psentence=sentence.lower()
    result=[]
    for x in setAlphabet:
        if x in psentence:
            result.append(True)
        else:
            result.append(False)
    if False in result:
        return False
    else:
        return True
sentence1=' Glib jocks quiz nymph to vex dwarf'
sentence2='Waltz, bad nymph, for quick jigs vex.'
sentence3= 'Sphinx of black quart, judge my vow.'
sentence4= 'How vexingly quick daft zebras jump!'
sentence5= 'The five boxing wizards jump quickly.'
sentence6= 'Jackdaws love my big sphinx of quartz.'
sentence7= 'Pack my box with five dozen liquor jugs.'
sentence8='abcdefghijklmnopqrstuvwxyz'
z1= is_pangram(sentence1)
z2= is_pangram(sentence2)
z3= is_pangram(sentence3)
z4= is_pangram(sentence4)
z5= is_pangram(sentence5)
z6= is_pangram(sentence6)
z7= is_pangram(sentence7)
z8=is_pangram(sentence8)
print(z1,z2,z3,z4,z5,z6,z7,z8,sep='\n')
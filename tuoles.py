simpletuple=(x,y)
x,y=simpletuple
newTuple=(y,x)
print(newTuple)
x,y = y,x
print(x,y)

if 'my first' in single:
    print('A value exist in a collection: ',single)
else:
    print('The value is not present i collection..',single)
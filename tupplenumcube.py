myList = [6, 2, 5 ,1, 4]
tupleList = [] 
for val in myList:
    myTuple = (val, (val*val*val))
    tupleList.append(myTuple)
print("The list of Tuples is " , str(tupleList))

import operator
mydict={}
while True:
    key=input("enter a key(or 'q' to quit):")
    if key=='q':
        break
    value=int(input("enter a value:"))
    mydict[key]=value
    print('orginal dictonary:',mydict)
    sd = dict(sorted(mydict.items(), key=operator.itemgetter(1)))
    print("Dictonary in ascending order by value:",sd)
    sd = dict(sorted(mydict.items(), key=operator.itemgetter(1), reverse=True))
    print("Dictonary in descending order by value:",sd)

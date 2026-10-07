mydict1={}
print("ENTER ELEMENTS OF FIRST DIE")
while True:
    key=input("enter a key(or 'q'to quit):")
    if key=='q':
        break
    value=int(input("enter a value"))
    mydict1[key]=value
    print("Enter element of second die")
    mydict2={}
    while True:
        key=input("enter a key(or 'q' to quit):")
        if key=='q':
            break
        value=int(input("enter a value:"))
        mydict2[key]=value
        print(mydict1|mydict2)

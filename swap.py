string1 = input("ENTER FIRST STRING: ")
string2 = input("ENTER SECOND STRING: ")
stringn = string2[0] + string1[1:] + "  " + string1[0] + string2[1:]
print(stringn)

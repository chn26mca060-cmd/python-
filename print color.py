clist1 = set()

clist2 = set()

n1 = int(input("ENTER THE NUMBER OF COLORS IN LIST1: "))
print("ENTER THE COLORS TO LIST1")

for x in range(n1):
    color=input()
    clist1.add(color)
n2 = int(input("ENTER THE NUMBER OF COLORS IN LIST2: "))
print("ENTER THE COLORS TO LIST2:")

for x in range(n2):
    color = input()
    clist2.add(color)

diff = clist1.difference(clist2)

print("COLORS IN LIST1 NOT IN LIST2:", diff)

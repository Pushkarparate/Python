for i in range(1,6):
    for space in range(0,6-i):
        print(" ",end=" ")
    for j in range(0,(2*i-1)):
        print("*",end=" ")
    print("\n")
for i in range(6,0,-1):
    for space in range(i,7-i):
        print(" ",end=" ")
    for j in range(0,(2*i-1)):
        print("*",end=" ")
    print("\n")

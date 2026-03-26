v=float(input("Enter the voltage: "))
r=float(input("Enter the resistance: "))
i=v/r
print("Current= ",i,"A")

if(i<0.5):
    print("Low Current")
elif 0.5<=i<=2:
    print("Normal current")
elif i>2:
    print("High current")
else:
    print("Invalid")








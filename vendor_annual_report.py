num=input("Enter numbers sperated by space: ")
num_list=num.split()
num_tuple=tuple(int(num1) for num1 in num_list)
print(num_tuple)
#length of tuple
print(len(num_tuple))
#print last item in tuple
print(num_tuple[-1])
#reverse tuple
print(num_tuple[::-1])
#yes or no
if 5 in num_tuple:
    print("Yes")
else:
    print("No")
        
#remove last and first and sort them then print
n=len(num_tuple)
if(n>=2):
    t=list(num_tuple[1:-1])
    t.sort()
    print(t)
else:
    print("length of tuple is too small")

        

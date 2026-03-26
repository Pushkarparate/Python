st=input("Enter a string: ")
count=0
alpha=0
space=0
lower=0
vowels="aeiouAEIOU"
for i in st:
    if i.isalpha():
        if i in vowels:
            count=count+1
        else:
            alpha=alpha+1
        
    elif i.isspace():
        space=space+1

    if i.islower():
        lower=lower+1
   
print("Vowels:",count)
print("Consonents:",alpha)
print("Lowercase:",lower)
print("spaces:",space)

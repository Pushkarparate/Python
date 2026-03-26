t=input("Enter elemnts seperated with spaces: ")
t_list=t.split()
t_tuple=tuple(int(n) for n in t_list)
print(t_tuple)
#total number of items
print(len(t_tuple))
#cheapest item
print(min(t_tuple))
#costiest item
print(max(t_tuple))
#price in ascending order
print(sorted(t_tuple))
#costly item sold on a day
print(t_tuple.count(max(t_tuple)))

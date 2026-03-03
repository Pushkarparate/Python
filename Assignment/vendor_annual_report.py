name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total = 0

for i in range(1, 13):
    amount = float(input(f"Enter purchase amount for month {i}: "))
    total += amount

average = total / 12

print("\n----- Annual Purchase Report -----")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", total)
print("Average Monthly Purchase:", average)

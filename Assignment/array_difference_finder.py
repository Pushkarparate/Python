n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

max_diff = abs(arr[0] - arr[1])
min_diff = abs(arr[0] - arr[1])

for i in range(n):
    for j in range(i + 1, n):
        diff = abs(arr[i] - arr[j])
        if diff > max_diff:
            max_diff = diff
        if diff < min_diff:
            min_diff = diff

print("\nMaximum Difference:", max_diff)
print("Minimum Difference:", min_diff)

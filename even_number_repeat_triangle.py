# Initialize vote count for 5 candidates
count = [0, 0, 0, 0, 0]
spoilt = 0

n = int(input("Enter total number of ballots: "))

for i in range(n):
    vote = int(input(f"Enter vote {i+1}: "))

    if 1 <= vote <= 5:
        count[vote - 1] += 1
    else:
        spoilt += 1

# Display results
print("\nElection Results:")
for i in range(5):
    print(f"Candidate {i+1}: {count[i]} votes")

print("Spoilt Ballots:", spoilt)

votes=["Red","Blue","Red","Red","Blue","Green","Blue","Blue","Blue"]
counts={}

for team in votes:
    if team not in counts:
        counts[team]=0
    counts[team]=counts[team]+1

    
print(counts["Red"])
print(counts)
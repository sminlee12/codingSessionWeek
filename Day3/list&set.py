scores=[72,72,68,60]
levels = set(scores)

for score in scores:
    levels.add(score)

print(len(levels))
print(68 in levels)
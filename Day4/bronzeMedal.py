N = int(input())
numlist = [int(input()) for _ in range(N)]

gold = max(numlist)
silver = max(score for score in numlist if score < gold)
bronze = max(score for score in numlist if score < silver)
bronzes = numlist.count(bronze)

print(bronze, bronzes)

values=[4,1,3,2]

for i in range(len(values)-1):
    if values[i] > values[i+1]:
        saved=values[i]
        values[i]=values[i+1]
        values[i+1]=saved

print(values)
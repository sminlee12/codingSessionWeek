Dusa = int(input("give Dusa"))
number=0
numbers=[]


for i in range(4):
     
    number=int(input("give number"))
    if number < Dusa:
        Dusa=number+Dusa
    elif number >= Dusa:
        break

print(Dusa)
                
   






# numlist = [6,2,5,13,1]
# dusa = numlist[0]

# for yobi in range(1,len(numlist)-1):
#     if dusa > yobi:
#         dusa=dusa+yobi
#     else:
#         break

# print(dusa)
name="" 
number=0
winnerName=""
winnerNumber=0

for i in range(4):
    name = input("Enter bidder's name  :")
    number = int(input("Enter bidding amount :"))
    if(number>winnerNumber):
        winnerNumber = number
        winnerName = name

print(winnerName)
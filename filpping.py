import random
class Coin:
    def __init__(self):
        self.slides=1
    def Toss_coin(self,n):
       for i in range(1,n):
         random_number=random.randint(0,1)
         print(random_number)
C=Coin()
X=int(input("enter the number of  coins you want to display"))
C.Toss_coin(X)


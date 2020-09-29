from random import randint, choice


class Die():
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        result = randint(1, self.sides)
        print(result)
        

class Lottery():
    
    def __init__(self):
        numbers = (34, 56, 78, 90, 11, 9, 8, 6, 5, 4, "A", "B", "C", "Z", "X")
        lottery = ""
        for i in range(1, 5):
            lottery += str(choice(numbers))
       
        self.lottery_num = lottery
        
    def get_lottery(self):
        print(self.lottery_num)
        return self.lottery_num
        
        
    
        
        
        
        
    
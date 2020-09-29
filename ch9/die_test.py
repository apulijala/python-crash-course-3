from std_library import * 
import unittest 

class DieTest(unittest.TestCase):
    def test_roll_die(self):
        ten_sided_die = Die(10)
        print("Ten sided Die")
        for i in range(1, 10):
            ten_sided_die.roll_die()
        
        print("Twenty sided Die")
        twenty_sided_die = Die(20)
        for i in range(1, 10):
            twenty_sided_die.roll_die()


    def test_lottery(self):
        lottery = Lottery()
        lottery_num = lottery.get_lottery()
        print(f"lotter number is {lottery_num}")
        lottery = "56X88"

    def test_lottery_analysis(self):
        counter = 1
        lottery = Lottery()
        while True:
            lottery_number = lottery.get_lottery()
            counter = counter + 1
            if lottery_number == "56X88":
                print(f"Lottery number matched {lottery_number}")
                break
                
            


if __name__ == "__main__":
    unittest.main()

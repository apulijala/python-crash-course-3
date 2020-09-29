from inheritence import * 
import unittest

class InheritanceTest(unittest.TestCase):
    def test_icecream_stand(self):
        flavors = ["Vanila", "Strawberry", "Mango"]
        icecream_stand = IceCreamStand("TuttyFruity", "Icecream", flavors)
        icecreams = icecream_stand.get_flavors()
        for icecream in icecreams:
            print(f"Icecream is {icecream} flavour")
    
    def test_show_privileges(self):
        privileges = ["can add post", "can delete post", "can ban user"]
        admin = Admin("Arvind", "Pulijala", privileges)
        privs = admin.show_privileges().get_privileges()

        
        for priv in privs: 
            print(f"privilege : {priv}")
            

        
        
        
if __name__ == "__main__":
    unittest.main()
  

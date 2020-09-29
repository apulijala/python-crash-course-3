

class Guest():
    def __init__(self, filename):
        self.filename = filename

    """
    10-3. Guest: 
    Write a program that prompts the user for their name. When they respond, write their name to a file 
    called guest.txt.
    """
    
    def prompt_user(self):
        try: 
            with open(self.filename, 'w') as filewriter:
                
                while True:
                    name = input("Please enter your name or enter quit: ")
                    if name.upper() == "QUIT":
                        break # will break out of the for loop
                    filewriter.write(name + "\n")
                    
        except FileNotFoundError as fe:
            pass

        """
            10-4. Guest Book: Write a while loop that prompts users for their name. When they enter their name, 
            print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. 
            Make sure each entry appears on a new line in the file.
        """
        
    def guest_book(self):
        # Code at the bottom was causing problem. 
        with open(self.filename, "a") as appender:
            # don't use break, as it is a bad practice. 
            while True:
                print("Outside the loop")
                name = input("Enter your name please or enter quit? ")
                if name.upper() == "QUIT":
                    break
                else: 
                    print(f"Jaya Guru Datta, {name}")
                    appender.write(name +  "\n")
    
    """
        10-5. Programming Poll: Write a while loop that asks people why they like programming. 
        Each time someone enters a reason, add their reason to a file that stores all the responses.
    """
    
    def programming_poll(self):
        with open(self.filename, "w") as writer:
            responses = []
            while True:
                response = input("What is your favorite programming language or enter quit ? ")
                if response.upper() == "QUIT":
                    break
                else:
                    responses.append(response + "\n")
            writer.writelines(responses)

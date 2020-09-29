""" 
10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what 
you’ve learned about Python so far. Start each line with the phrase In Python you can. . .. 
Save the file as learning_python.txt in the same directory as your exercises from this chapter. 
Write a program that reads the file and prints what you wrote three times. 
Print the contents once by reading in the entire file, once by looping over the file object, 
and once by storing the lines in a list and then working with them outside the with block.
8:04. Except get it working by 8:21
Completed at 8:33
"""

class OpeningFiles():
    def __init__(self, filename):
        self.filename = filename
        
    
    def read_file_entirely(self):
        
        with open(self.filename) as filename:
            content = filename.read()
            print(content)

        
        
        
    def read_lines_from_file(self):
        with open(self.filename) as filename:
            for line in filename.readlines():
                print(f"{line.rstrip()}")
    
    def read_lines_from_array(self):
        with open(self.filename) as filename:
            lines = filename.readlines()
            for line in lines:
                print(f"{line.rstrip()}")
                
    def replacer(self, msg):
        print(f"\nReplacing Text\n")
        with open(self.filename) as filename:
            lines = filename.readlines()
            for line in lines:
                line = line.replace(r"python", "c").strip()
                line = line.replace(r"Python", "C").strip()
                print(f"{line}")
                
        

"""
    You can use the replace() method to replace any word in a string with a different word. 
    Here’s a quick example showing how to replace 'dog' with 'cat' in a sentence: 
"""
    
    

  


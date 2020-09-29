import unittest
from learn_exceptions import * 


class FileTester(unittest.TestCase):
    
    def setUp(self):
        filename = "python_lines.txt"
        self.fileopener = OpeningFiles(filename)
    
    def test_read_file_entirely(self):
        self.fileopener.read_file_entirely()
        
    
    def test_read_lines_from_file(self):
        self.fileopener.read_lines_from_file()
        
    def test_read_lines_from_array(self):
        print("\nTesting the read lines from read_lines_from_array\n")
        self.fileopener.read_lines_from_array()
    
    def test_replacer(self):
        msg = "c"
        self.fileopener.replacer(msg)
        
        
    

if __name__ == "__main__":
    unittest.main()

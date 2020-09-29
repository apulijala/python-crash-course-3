import json

class JsonDumps():
    def __init__(self, jsonfile):
        self.jsonfile = jsonfile
        

    def write_favorite_data_structures(self):
        my_array = ["red", "green", "yellow"]
        my_hash = {
            "Name" : "Arvind K. Pulijala", 
            "MyArray" : my_array
        }
        try: 
            with open("hello.json", "w") as f:
                # json.dump(my_array, f)
                json.dump(my_hash, f)
                
        except FileNotFoundError:
            pass
    
    def read_favorite_data_structure(self):
        try: 
            with open("hello.json", "r") as f:
                # json.dump(my_array, f)
                myhash = json.load(f)
                print(myhash[0]["tags"])
        except FileNotFoundError:
            pass
        

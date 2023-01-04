#The definition of the file storage
import json

class FileStorage:
    #The file storage class
    __file_path = ""
    __objects = {}

    def all(self):
        #returns the dictionary __objects
        return __objects
    
    def new(self, obj):
        #sets in __objects the obj with key <obj class name>.id
        __objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        #serializes __objects to the JSON file (path: __file_path)
        with open(__file_path, "w") as f:
            json.dump(f, __objects)

    def reload(self):
        #deserializes the JSON file to __objects (only if the JSON file (__file_path)
        try:
            __objects = json.load(__file_path)
        except:
            pass
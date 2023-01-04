#The definition of the file storage
import json

class FileStorage:
    #The file storage class
    __file_path = ""
    __objects = {}

    def all(self):
        #returns the dictionary __objects
        return self.__class__.__objects
    
    def new(self, obj):
        #sets in __objects the obj with key <obj class name>.id
        self.__class__.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        #serializes __objects to the JSON file (path: __file_path)
        try:
            with open(self.__class__.__file_path, "w") as f:
                json.dump(f, self.__class__.__objects)
        except:
            return True

    def reload(self):
        #deserializes the JSON file to __objects (only if the JSON file (__file_path)
        try:
            self.__class__.__objects = json.load(self.__class__.__file_path)
        except:
            pass

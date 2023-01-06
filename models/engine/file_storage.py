#The definition of the file storage
import json

class FileStorage:
    #The file storage class
    __file_path = "file.json"
    __objects = {}

    def all(self):
        #returns the dictionary __objects
        return self.__class__.__objects
    
    def new(self, obj):
        #sets in __objects the obj with key <obj class name>.id
        self.__class__.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
        
    def save(self):
        #serializes __objects to the JSON file (path: __file_path)

        my_obj_dict = {}
        for key in FileStorage.__objects:
            my_obj_dict[key] = FileStorage.__objects[key].to_dict()
        f = open(self.__class__.__file_path, "w")
        json.dump(my_obj_dict, f)
        f.close()

    def reload(self):
        #deserializes the JSON file to __objects (only if the JSON file (__file_path)
        try:
            self.__class__.__objects = json.load(self.__class__.__file_path)
        except:
            pass

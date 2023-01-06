#The definition of the file storage
import json

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)


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
        from models.base_model import BaseModel
        #deserializes the JSON file to __objects (only if the JSON file (__file_path)
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            objects = json.loads(f)
            FileStorage.__objects = {}
            for key in objects:
                FileStorage.__objects[key] = BaseModel(**objects[key])

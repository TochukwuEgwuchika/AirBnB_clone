#BaseModel class definition
import uuid
import datetime


import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
#parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)
from models.__init__ import storage

class BaseModel:
    #Basemodel class
    def __init__(self, *args, **kwargs):
        #Initialize the object
        if len(kwargs) != 0:
            self.id = str(kwargs["id"])
            self.created_at = datetime.datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        #return string representation of the class
        return f"[{self.__class__.__name__}] ({self.id}) self.__dict__)"

    def save(self):
        #update the object
        self.updated_at = datetime.datetime.now()
        storage.save()
    
    def to_dict(self):
        #returns dictionary representation of an object
        the_dict = self.__dict__
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = str(the_dict["created_at"].isoformat(sep="T", timespec="auto"))
        the_dict["updated_at"] = str(the_dict["updated_at"].isoformat(sep="T", timespec="auto"))
        return the_dict

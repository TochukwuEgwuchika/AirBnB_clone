#BaseModel class definition
import uuid
import datetime

class BaseModel:
    #Basemodel class
    def __init__(self):
        #Initialize the object
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        #return string representation of the class
        return f"[{self.__class__.__name__}] ({self.id}) self.__dict__)"

    def save(self):
        #update the object
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        #returns dictionary representation of an object
        the_dict = self.__dict__
        the_dict["__class__"] = self.__class__.__name__
        the_dict["created_at"] = str(the_dict["created_at"].isoformat(sep="T", timespec="auto"))
        the_dict["updated_at"] = str(the_dict["updated_at"].isoformat(sep="T", timespec="auto"))
        return the_dict

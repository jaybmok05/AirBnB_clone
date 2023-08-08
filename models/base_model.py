"""Defining a BaseModel class"""
from datetime import datetime
import uuid


class BaseModel(object):
    """A basemodel class that defines all common
    attributes/methods for other classes.

    Attributes:
        id (string):  assign with an uuid when an instance is created.
        created_at (datetime): the current datetime when an instance is created
        updated_at (datetime): the current datetime when an instance is created
        and it will be updated every time you change your object
    """
    def __int__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        this function should print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        print("[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__))

    def save(self):
        """A function that updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        return {
            **self.__dict__,
            '__class__': __class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
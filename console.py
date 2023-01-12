#!/usr/bin/python3

"""
console base for the application
"""
import cmd

from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """implementation of the cmd class"""
    prompt = "(hbnb)"

    class_dict = {
            "BaseModel" : BaseModel
            }

    def do_quit(self, tokens):
        """quit when quit is entered"""
        return True

    def do_EOF(self, tokens):
        """quit when EOF is entered"""
        return True

    def emptyline(self):
        """when an empty line is entered"""
        pass

    def do_create(self, tokens):
        """create objects of the required class"""

        if len(tokens.split()) == 0:
            print("** class name missing **")
        elif tokens.split()[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        else:
            myObj = BaseModel()
            myObj.save()
            print(myObj.id)

    def do_show(self, tokens):
        """ Prints the string representation of an instance based on the class name and id """
        print(tokens)
        if len(tokens.split()) == 0:
            print("** class name missing **")
        elif tokens.split()[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(tokens.split()) == 1:
            print("** instance id missing **")
        elif tokens.split()[1] not in storage.all().keys():
            print("** no instance found **")
        else:
            pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()

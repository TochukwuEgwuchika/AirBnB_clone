#!/usr/bin/python3

"""
console base for the application
"""
import cmd

from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """implementation of the cmd class"""
    prompt = "(hbnb)"

    class_dict = {
            "BaseModel" : BaseModel;
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
        if len(tokens.split()) != 2:
            print("** class name missing **")
        elif tokens.split()[1] not in class_dict.keys():
            print("** class doesn't exist **")
        else:
            myObj = BaseModel()
            myObj.save()
            print(myObj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

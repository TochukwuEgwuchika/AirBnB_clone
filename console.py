#!/usr/bin/python3

"""
console base for the application
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """implementation of the cmd class"""
    prompt = "(hbnb)"

    def do_quit(self, s):
        """quit when quit is entered"""
        return True

    def do_EOF(self, s):
        """quit when EOF is entered"""
        return True

    def emptyline(self):
        """when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

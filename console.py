#!/usr/bin/python3

import cmd

#contains the entry point of the command interpreter

class HBNBCommand(cmd.Cmd):
    #console class
    prompt = "(hbnb)"

    def do_quit(self, s):
        #quit when quit is entered
        return True

    def do_EOF(self, s):
        #quit when EOF is entered
        return True

    def emptyline(self, s):
        #when an empty line is entered
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

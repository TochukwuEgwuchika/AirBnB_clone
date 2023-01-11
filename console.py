#!/usr/bin/python3
#contains the entry point of the command interpreter

class HBNBCommand(cmd.Cmd):
    #console class
    prompt = "(hbnb)"

    def do_quit(self):
        #quit when quit is entered
        return

    def do_EOF(self):
        #quit when EOF is entered
        return

    def emptyline(self):
        #when an empty line is entered
        pass

    if __name__ == '__main__':
        HBNBCommand().cmdloop()

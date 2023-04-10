#!/usr/bin/python3
"""Defines entry point of command Interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handles end of file"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Print empty line"""
        pass

    def do_create(self, line):
        """Creates/saves an instance and prints its id"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            ins = storage.classes()[line]()
            ins.save()
            print(ins.id)

    def do_show(self, line):
        """Prints string representation of an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line != "":
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                p = [str(obj) for key, obj in storage.all().items()
                        if type(obj).__name__ == words[0]]
                print(p)
        else:
            nl = [str(obj) for key, obj in storage.all().items()]
            print(nl)

    def do_update(self, line):
        """Updates an instance"""






if __name__ == '__main__':
    HBNBCommand().cmdloop()

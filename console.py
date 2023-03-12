#!/usr/bin/python3
"""Defines entry point of command Interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Interpreter class"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handles end of file"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Print empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

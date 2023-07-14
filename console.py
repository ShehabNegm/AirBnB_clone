#!/usr/bin/python3
"""Defines HBNBCommand class"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the console"""
        print()
        return True

    def emptyline(self):
        """Handles empty lines"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

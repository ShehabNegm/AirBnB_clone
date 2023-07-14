#!/usr/bin/python3
"""Defines HBNBCommand class"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

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

    def do_create(self, arg):
        """create new instance of arg and save it so json file"""

        if not arg:
            print("** class name missing **")

        elif arg not in self.classes:
            print("** class doesn't exist **")

        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

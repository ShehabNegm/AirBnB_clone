#!/usr/bin/python3
"""Defines HBNBCommand class"""
import cmd
from models import storage
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

    def do_show(self, arg):
        """Prints the string representation of inst. based on the cls name"""

        args = arg.split()
        if not args:
            print("** class name missing **")

        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

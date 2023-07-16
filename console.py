#!/usr/bin/python3
"""Defines HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

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
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance"""
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
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Displays all instances of a class
        or all instances if no class name is given
        """
        args = arg.split()
        instances = []
        if not args:
            for value in storage.all().values():
                instances.append(str(value))
            print(instances)

        elif args[0] in self.classes:
            class_name = args[0]
            for key, value in storage.all().items():
                if class_name in key:
                    instances.append(str(value))
            print(instances)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif (args[0] + "." + args[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            instance = storage.all()[key]
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            value = cast(arg3)
            setattr(instance, args[2], value)
            storage.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        count = 0

        for object_1 in storage.all().values():
            if object_1.__class__.__name__ == class_name:
                count += 1

        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3

import cmd
import re
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class represents the command-line
    interface for the AirBnB clone program.
    It provides various commands for creating,
    showing, updating, and deleting instances.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, line):
        print()
        return True

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def default(self, line):
        print(f"Unrecognized command: {line}. Type 'help' for assistance.\n")

    def do_help(self, line):
        super().do_help(line)

    def do_create(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            obj = self.CLASSES[class_name]()
            obj.save()
            print(obj.id)
        except ImportError:
            print("** class doesn't exist **")

    def do_show(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        args = line.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            instances = [
                str(obj) for key, obj in storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)

    def do_update(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s(".*"|[^"]\S*)?)?)?)?'
        match = re.search(rex, line)

        if not match:
            print("** invalid command format **")
            return

        classname, uid, attribute, value = match.groups()

        if classname not in self.CLASSES:
            print("** class doesn't exist **")
            return
        elif not uid:
            print("** instance id missing **")
            return

        key = f"{classname}.{uid}"
        if key not in storage.all():
            print("** no instance found **")
            return
        elif not attribute:
            print("** attribute name missing **")
            return
        elif not value:
            print("** value missing **")
            return

        obj = storage.all()[key]
        setattr(obj, attribute, value)
        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

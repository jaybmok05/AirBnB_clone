#!/usr/bin/python3
"""
Defines methods that serve as command handlers
for the command interpreter
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Custom commad interpreter for the HBNB application"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF(Ctrl-D) is encountered"""
        print()
        return True

    def emptyline(self):
        """ Do not do anything on an empy line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel/User, saving it to the JSON file
        and print the id
        Usage: create <class name>
        """
        if not  arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id
        Usage: create <class name> <id>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id,
        save the changes into the JSON file
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based on class name
        """
        args = shlex.split(arg)
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] in storage.classes():
            print([str(obj) for key, obj in storage.all().items() if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or 
        updating attribute, the changes are saved into the JSON file
        
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        setattr(instance, args[2], args[3])
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

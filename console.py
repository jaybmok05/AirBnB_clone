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
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        if not arg:
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
            print([str(obj) for key, obj in storage.all().values()])
        elif args[0] in storage.classes():
            print([str(obj) for key, obj in storage.all().items()
                  if key.startswith(args[0])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Update an instance based on the class name and id by adding or
        updating attribute, the changes are saved into the JSON file

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) < 4:
            print("** Usage: update <class name> <id> \
                    <attribute name> <attribute value **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, arg):
        """
        This command will return number of <class name>
        in the file storage
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] in storage.classes():
            counted = 0
            for key, obj in storage.all().items():
                if key.startswith(args[0]):
                    counted += 1
            print(int(counted))
        else:
            print("** class name doesnt exist **")

    def precmd(self, line):
        """
        This method is called before executing each command
        It modifies the line if necessary
        """
        if line.endswith(".all()"):
            parts = line.split(".")
            if len(parts) == 2:
                return "all " + parts[0]

        if line.endswith(".count()"):
            parts = line.split(".")
            if len(parts) == 2:
                return "count " + parts[0]

        if line.endswith(")"):
            parts = line.split("(")
            if len(parts) == 2:
                command_parts = parts[0].split(".")
                if len(command_parts) == 2 and command_parts[1] == "update":
                    class_name = command_parts[0]
                    args = parts[1].rstrip(")").split(", ")
                    if len(args) == 3:
                        instance_id, attribute_name, attribute_value = args
                        return f"update {class_name} {instance_id} \
                                        {attribute_name} {attribute_value}"

        if line.endswith(")"):
            parts = line.split("(")
            if len(parts) == 2:
                command_parts = parts[0].split(".")
                if len(command_parts) == 2 and command_parts[1] == "show":
                    # Extract class name and instance id from the line
                    class_name, instance_id = command_parts[0],\
                                              parts[1].rstrip(")")
                    # Format the command in the show format
                    return f"show {class_name} {instance_id}"
                elif len(command_parts) == 2 and command_parts[1] == "destroy":
                    class_name, instance_id = command_parts[0],\
                                              parts[1].rstrip(")")
                    return f"destroy {class_name} {instance_id}"
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()

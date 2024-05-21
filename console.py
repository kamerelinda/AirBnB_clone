#!/usr/bin/python3
# contains the entry point of the command interpreter:

import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        'EOF command to exit the program'
        print("")  # Print a newline before exiting
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it (to the JSON file), and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        try:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

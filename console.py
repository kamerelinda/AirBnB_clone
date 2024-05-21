#!/usr/bin/python3
# contains the entry point of the command interpreter:

import cmd
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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
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
        obj_dict = storage.all()
        obj = obj_dict.get(key)
        if obj is None:
            print("** no instance found **")
        else:
            del obj_dict[key]  # Remove the object from the dictionary
            storage.save()  # Save the changes to the JSON file

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        obj_list = []
        if args:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.startswith(class_name):
                    obj_list.append(str(obj))
        else:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name, obj_id, attr_name, attr_value = args[0], args[1], args[2], args[3]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return

        # Attempt to cast the value to the correct type
        try:
            attr_type = type(getattr(obj, attr_name))
            if attr_type == int:
                attr_value = int(attr_value)
            elif attr_type == float:
                attr_value = float(attr_value)
            else:
                attr_value = str(attr_value)
        except AttributeError:
            print("** attribute doesn't exist **")
            return
        except ValueError:
            print("** value type mismatch **")
            return

        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        count = sum(1 for key in storage.all() if key.startswith(class_name))
        print(count)

    def default(self, line):
        """Handle <class name>.all() commands"""
        args = line.split('.')
        if len(args) == 2:
            class_name, command = args
            if command == "all()":
                self.do_all(class_name)
                return
            elif command == "count()":
                self.do_count(class_name)
                return
            elif command.startswith("show(") and command.endswith(")"):
                obj_id = command[5:-1].strip('"')
                self.do_show(f"{class_name} {obj_id}")
                return
            elif command.startswith("destroy(") and command.endswith(")"):
                obj_id = command[8:-1].strip('"')
                self.do_destroy(f"{class_name} {obj_id}")
                return
            elif command.startswith("update(") and command.endswith(")"):
                params = command[7:-1].split(", ")
                if len(params) == 3:
                    obj_id = params[0].strip('"')
                    attr_name = params[1].strip('"')
                    attr_value = params[2].strip('"')
                    self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")
                    return
        print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

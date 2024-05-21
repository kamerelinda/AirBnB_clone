#!/usr/bin/python3
# contains the entry point of the command interpreter:

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

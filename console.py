#!/usr/bin/python3
"""
The command interpreter for the (hbnb)
It consists of:
    - quit and EOF to exit the program
    - help
    - a custom prompt: (hbnb)
    - an empty line + ENTER shouldn’t execute anything
Commands to be entered:
    - create
    - show
    - destroy
    - all
    - update
"""
import cmd
import models
import shlex
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Entry point of the interpreter"""
    prompt = "(hbnb) "
    __classes = [
            "User",
            "State",
            "Review",
            "Place",
            "City",
            "BaseModel",
            "Amenity"
    ]

    def do_EOF(self, args):
        """Handles end-of-file (Ctrl-D/Ctrl-Z) input"""
        return True

    def do_create(self, args):
        """
        - Creates a new instance of BaseModel
        - saves it (to the JSON file) and prints the id
        - Usage: create <class>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_creation = eval(args[0] + '()')
            models.storage.save()
            print(new_creation.id)
        
    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name
        - If the class name is missing, print ** class name missing **
        - If the class name doesn’t exist, print ** class doesn't exist **
        - If the id is missing, print ** instance id missing **
        - If the instance of the class name doesn’t exist for the id, print ** no instance found **
        - Usage: show <class name> <id>
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
         Deletes an instance based on the class name and id
         - If the class name is missing, print ** class name missing **
         - If the class name doesn’t exist, print ** class doesn't exist **
         - If the id is missing, print ** instance id missing **
         - If the instance of the class name doesn’t exist for the id, print ** no instance found **
         - Usage: destroy <class name> <id>
         """
        args = args.split()
        objects = models.storage.all()
        
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[1]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')
    
    def do_all(self, args):
        """
        It prints all string representation of all instances based or not on the class name
        - The printed result must be a list of strings
        - If the class name doesn’t exist, print ** class doesn't exist **
        """
        args = args.split()
        objects = models.storage.all()
        new_list = []
        
        if len(args) == 0;
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
         else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
            print(new_list)
    
    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        - If the class name is missing, print ** class name missing **
        - If the class name doesn’t exist, print ** class doesn't exist **
        - If the id is missing, print ** instance id missing **
        - If the value for the attribute name doesn’t exist, print ** value missing **
        - Usage update <class name> <id> <attribute name> "<attribute value>"
        """
        objects = models.storage.all()
        args = args.split(" ")
        
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            obj = objects.get(key_find, None)

        if not obj:
                print("** no instance found **")
                return
        setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
        models.storage.save()
    
    def emptyline(self):
        """
        This method overrides the default behavior of executing the last non-empty command
        -Nothing is executed in response to an empty line
        """
        pass
    
    def check_class_name(self, name=""):
        """Check if the user input contains a class name and class ID"""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Checks if the user input contains a valid class ID"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True
    
    def found_class_name(self, name=""):
        """Search for a class within the given name"""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

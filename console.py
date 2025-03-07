#!/usr/bin/python3
"""
Module: Console
This is a console for the AirBnB clone that
is resposible for validating the file storage
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import theClasses
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNB class console command intepreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Pops the Prompt in the next line
        """
        pass

    def do_create(self, args):
        """
        Creates a new object
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        token = args.split()

        try:
            newInstance = eval(token[0])()
            newInstance.save()
            print(newInstance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        Prints a string representation of a new object
        """
        token = args.split()

        if len(token) == 0:
            print("** class name missing **")
            return
        if len(token) == 1:
            print("** instance id missing **")
            return
        try:
            eval(token[0])
        except:
            print("** class doesn't exist **")

        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            value = objDict[keyId]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an object with specified id
        """
        token = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return
        if token[1] == 0:
            print("** instance id missing **")

        try:
            eval(token[0])
        except:
            print("** class doesn't exist **")
        objDict = storage.all()
        keyId = token[0] + "." + token[1]

        try:
            del objDict[keyId]
        except:
            print("** no instance found **")
        storage.save()

    def do_all(self, arg):
        """
        Prints all objects in a given class
        """

        if not arg:
            print("** class name missing **")
            return

        token = arg.split()

        if token[0] not in theClasses:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            newList = []

            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                if ob_name == token[0]:
                    newList += [val.__str__()]
            print(newList)

    def do_update(self, args):
        """
        Updates an object based on the class name and id
        """

        if not args:
            print("** class name missing **")
            return

        token = args.split()

        if token[0] not in theClasses:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, val in all_objs.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == token[0] and ob_id == token[1].strip('"'):
                    if len(token) == 2:
                        print("** attribute name missing **")
                    elif len(token) == 3:
                        print("** value missing **")
                    else:
                        setattr(val, token[2], token[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_EOF(self, args):
        """
        End_Of_File - Kills the console
        """
        return True

    def do_quit(self, args):
        """
        Kills the console
        """
        return True

if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()

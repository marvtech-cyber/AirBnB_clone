#!/usr/bin/python3
"""
This module contains the code for the custom
command interpreter.
"""
import cmd
from multiprocessing.sharedctypes import Value
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models import storage
valid_inst = {'BaseModel': BaseModel, 'User': User, 'State': State,
              'City': City, 'Amenity': Amenity, 'Place': Place,
              'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    This class is the foundation for the interpreter.
    """
    prompt = '(hbnb) '

    def precmd(self, line):
        """Reformat the comand line for advanced command syntax.
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        """

        _cmd = _cls = _args = ""
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            pline = line[:]
            _cls = pline[:pline.find('.')]
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            _args = pline[pline.find('(') + 1 : pline.find(')')]
            _args = _args.split(', ')
            if _args:
                for i in range(len(_args)):
                    _args[i] = _args[i].strip('"')
                line = ' '.join([_cmd, _cls] + _args)
        except exception as mess:
            pass
        finally:
            return line


    def do_quit(self, *args):
        """
        This method exits the interpreter if the user
        types the command "quit".
        """
        quit()

    def do_EOF(self, *args):
        """
        This method exits the interpreter if the user
        types the EOF command (CTRL+D).
        """
        print()
        raise SystemExit

    def emptyline(self):
        """
        This method eliminates the newline from
        emptyline + ENTER.
        """
        pass

    def do_create(self, arg):
        """
        This method creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id.
        """
        if len(arg) < 1:
            print("** class name missing **")
        elif arg in valid_inst.keys():
            new = valid_inst[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        This method prints the string representation of
        an object based on the class name and id.
        """
        args2 = args.split(' ')
        if args == "":
            print("** class name missing **")
        elif args2[0] in valid_inst.keys():
            if len(args2) < 2:
                print("** instance id missing **")
            else:
                item_search = args2[0] + "." + args2[1]
                item_all = storage.all()
                if item_search in item_all:
                    print(item_all[item_search])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        This method deletes an instance based on the
        class name and id, and saves the change into
        the JSON file.
        """
        args2 = args.split(' ')
        if args == "":
            print("** class name missing **")
        elif args2[0] in valid_inst.keys():
            if len(args2) < 2:
                print("** instance id missing **")
            else:
                item_search = args2[0] + "." + args2[1]
                item_all = storage.all()
                if item_search in item_all:
                    del item_all[item_search]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        This method prints a string representation
        of all objects based on the class name given
        or all objects if no class given.
        """
        if arg == "":
            for k in storage.all():
                print([str(storage.all()[k])])
        elif arg not in valid_inst.keys():
            print("** class doesn't exist **")
        else:
            for k, v in storage.all().items():
                if arg == v.__class__.__name__:
                    print([str(storage.all()[k])])

    def do_update(self, args):
        """
        This method updates an instance based on the class
        name and id.
        """
        args2 = args.split(' ')
        if not args:
            print("** class name missing **")
        elif len(args2) < 2:
            print("** instance id missing **")
        elif len(args2) < 3:
            print("** attribute name missing **")
        elif len(args2) < 4:
            print("** value missing **")
        elif args2[0] not in valid_inst:
            print("** class doesn't exist **")
        else:
            item_search = args2[0] + "." + args2[1]

            item_all = storage.all()
            if item_search in item_all:
                setattr(storage.all()[item_search],
                        args2[2], args2[3].strip('\'"'))
                storage.save()
            else:
                print("** no instance found **")

    def do_count(self, args):
        """
        This method count number of instance.
        """
        count = 0
        for k, v in storage._FileStorage__objects.items():
            if args == k.split('.')[0]:
                count += 1
            print(count)

    def help_count(self):
        """..."""
        print("Usage: count <class_name>")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

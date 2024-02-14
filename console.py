#!/usr/bin/python3
"""The command line interprater"""
import cmd
from models.base_model import BaseModel
from models import storage
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The command line"""
    intro = "Welcome to the command line"
    prompt = '(hbnb) '

    list_of_classes = [
        "BaseModel"
    ]

    missing_class = "** class name missing **"
    non_existant_class = "** class doesn't exist **"
    missing_id = "** instance id missing **"
    no_instance = "** no instance found **"

    def do_EOF(self, arg):
        """Handle EOF"""
        return True

    def do_quit(self, arg):
        """Ends the command line"""
        return True

    def do_create(self, args):
        """Create objects"""
        # Check if args contains only whitespace
        if not args.strip():
            print(self.missing_class)
            return

        class_obj = args.split()[0]

        if class_obj in self.list_of_classes:
            obj_instance = eval(class_obj)()
            obj_instance.save()
            print(obj_instance.id)
        else:
            print(self.non_existant_class)

    def do_show(self, args):
        """prints the string rep of an object with the given id"""
        # Check if args contains only whitespace
        if not args.strip():
            print(self.missing_class)
            return

        if not args:
            print(self.missing_class)
            return

        if len(args) < 2:
            print(self.missing_id)
            return

        class_name = args.split()[0]
        obj_id = args.split()[1]

        if class_name not in self.list_of_classes:
            print(self.non_existant_class)
            return

        if not obj_id:
            print(self.missing_id)
            return

        obj_key = f"{class_name}.{obj_id}"
        obj = storage.all().get(obj_key)

        if obj:
            print(obj)
        else:
            print(self.no_instance)



if __name__ == '__main__':
    HBNBCommand().cmdloop()

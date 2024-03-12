#!/usr/bin/python3

import cmd

"""cclass that defines console functionalities"""

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a newline for better UX
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass



     def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
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
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        else:
            try:
                class_name = args[0]
                if class_name not in globals():
                    print("** class doesn't exist **")
                    return
                print([str(obj) for key, obj in storage.all().items() if key.split('.')[0] == class_name])
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            setattr(storage.all()[key], attr_name, attr_value)
            storage.save()
        except Exception as e:
            print(e)

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a newline for better UX
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()

# Variable argument
def handle_var_args(f_args, *args):
    print("{} {}".format("Function argument: ", f_args))

    for arg in args:
        print("{} {}".format("Variable arguments: ", arg))

    print("{} {}".format("Variable arguments: ", args))

handle_var_args("Hello", "My", "Name", "Is", "Khan")

# Keyworded argument
def handle_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} : {1}".format(key, value))

handle_kwargs(Name="Praveen", Age="35", Sex="Male")

def accept_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ("1", "Two", "3")
accept_args_kwargs(*args)

## Note change in sequence for named arguments
kwargs = {"arg3" : 3, "arg1" : 1, "arg2" : "Two"}

accept_args_kwargs(**kwargs)
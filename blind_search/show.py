import inspect
from colorama import Fore, Back, Style

def show(*arg):
    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')
    
    for i in range(len(args)):
        if args[i].find('=') != -1:
            name = args[i].split('=')[1].strip()
        
        else:
            name = args[i]

        print(name + ": " + str(arg[i]), end="," if i != len(args) - 1 else "")
    print()

    return
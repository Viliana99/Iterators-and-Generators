from functools import wraps

def check_arguments(*args1):
    def decor(func):
        @wraps(func)
        def wrapper(*args):
            if len(args1) > len(args):
                raise TypeError
            for i in range(len(args1)):
                if not isinstance(args[i], args1[i]):
                    raise TypeError
            func(*args)
        return wrapper
    return decor



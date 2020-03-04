from functools import wraps

def  substitutive(func):
    @wraps(func)
    def wrapper(*args):
        @wraps(func)
        def dop_func(*dop_args):
            return wrapper(*(args + dop_args))#func(*(args + dop_args))
            
        if len(args) > func.__code__.co_argcount:
            raise TypeError
        try:
            func(*args)
        except:
            return dop_func
    return wrapper
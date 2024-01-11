def foo(func):
    def new_func(*args, **kwargs):
        print('Doing some stuff before instantiation')
        func(*args, **kwargs)

    return new_func

class Bar:
    def __init__(self):
        print("In initiator")


Bar.__init__ = foo(Bar.__init__)
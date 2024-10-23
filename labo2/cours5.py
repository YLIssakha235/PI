from  time import time
def timeit(f):
    def wrapper(*args, **kwargs):
        start = time()
        ret = f(*args, **kwargs)
        print('time: {}'.format(time() - start))
        return ret
    return wrapper()

@timeit
def sayhello():
    for  i in range(100000):
        print(i)
sayhello()

def checktypes(*types):
    def decorator(f):
        def wrapper(*args):
            for arg, type in zip(args, types):
                if not isinstance(arg,type):
                    raise TypeError('{} is not a {}'.format(arg,type))
            return f(*args)
        return wrapper
    return decorator

@checktypes(int,int)
def add(a,b):
    return a+b

print(add(4, 3))

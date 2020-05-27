from time import time

def time_decorator(func): 
    def inner(*args, **kwargs): 
          
        t1 = time()
          
        returned_value = func(*args, **kwargs)
        
        t2 = time()
        elapsed = t2 - t1
        
        print(f'Elapsed time is {elapsed} seconds.')
        print(20*"*")
        return returned_value 
          
    return inner 
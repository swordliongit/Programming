

def func(item, queue):
    
    res = func_depth_1(item)
    queue.put(res)
    
    
def func_depth_1(item):
    return func_depth_2(item)

def func_depth_2(item):
    return item+1
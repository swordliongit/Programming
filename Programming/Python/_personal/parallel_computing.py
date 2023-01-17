# pip install graphics.py -> used in the course

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import perf_counter, sleep


def func(id):
    print(f"Started {id}")
    for _ in range(10000000):
        pass
    return f"Done {id}"

def main():
    
    first_list_i = [1,2,3,4,5]
    second_list_i = [5,4,3,2,1]
    
    var = 5
    
    import itertools
    
    futures = []
    
    start = perf_counter()

    with ThreadPoolExecutor() as executor:
        results = executor.map(func, [i for i in range(50)])
        
        for res in results:
            print(res)
            
    end = perf_counter()
    
    print(end-start)
main()
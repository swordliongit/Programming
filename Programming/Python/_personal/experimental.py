from threading import Thread
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor, wait




def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    # print( f'Done with task {id}')
    return f'Done with task {id}...'

start = perf_counter()


with ThreadPoolExecutor() as executor:
    # f1 = executor.submit(task, 1)
    # f2 = executor.submit(task, 2)
    
    results = executor.map(task, [i for i in range(50)])
    
    # wait(results)
    for result in results:
        print(result)

    # print(f1.result())
    # print(f2.result())    

finish = perf_counter()

print(f"It took {finish-start} second(s) to finish.")

# start = perf_counter()

# tlist = []

# for i in range(50):
#     t = Thread(target=task, args=(i,))
#     tlist.append(t)
#     t.start()

# for t in tlist:
#     t.join()

# finish = perf_counter()

# print(f"It took {finish-start} second(s) to finish.")
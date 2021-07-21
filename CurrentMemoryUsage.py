#Trace the current memory usage by the Python script. 

import tracemalloc

tracemalloc.start()
#CODE
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
tracemalloc.stop()


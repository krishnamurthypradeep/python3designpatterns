from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Executing task {n}")
    time.sleep(1)
    print(f"Task {n} completed")

with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(10):
        executor.submit(task,i)   
        
# lazy Initialization Pattern
# Reducing initial load time
# Conserve System Resources
# Enhancing User Experience         
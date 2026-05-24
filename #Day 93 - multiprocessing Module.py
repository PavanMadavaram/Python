#Day 93 - multiprocessing Module 
from multiprocessing import Process, current_process
import os

def worker(name):
    print(f"{name} running in process {current_process().name} (pid={os.getpid()})")

if __name__ == "__main__":
    p1 = Process(target=worker, args=("Task-1",))
    p2 = Process(target=worker, args=("Task-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes finished")
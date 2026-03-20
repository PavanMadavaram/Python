#Day 44 - Context Helper
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"Time taken: {self.end - self.start:.2f}s")

with Timer():
    total = 0
    for i in range(1000000):
        total += i

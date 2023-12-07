import time

def measure_decorator(function):
    def measure():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"speed: {end_time - start_time}")
    return measure

@measure_decorator
def fast_function():
    for i in range(1000):
        i * i

@measure_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()

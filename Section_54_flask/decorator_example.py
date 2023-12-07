import time

def delay_decorator(function):
    def delay():
        time.sleep(2)
        function()
    return delay

@delay_decorator
def say_name():
    print("Duncan")

@delay_decorator
def say_hello():
    print("Hello")

say_hello()
say_name()

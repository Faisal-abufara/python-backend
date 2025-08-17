def MyDocr(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} has been called {wrapper.call_count} time(s)")
        return func(*args, **kwargs)
    
    wrapper.call_count = 0
    return wrapper

@MyDocr
def say_hello():
    print("Hello!")

@MyDocr
def add(a, b, c):
    return a + b +c

say_hello()
say_hello()
print(add(3, 4,5, name='anaser'))
print(add(10, 5,10))
print(add(7,5,8))

print(f"say_hello was called {say_hello.call_count} time(s)")
print(f"add was called {add.call_count} time(s)")
def decorator(func):
    def wrapper(a):
        result = func(a)
        return result + 3
    return wrapper


@decorator
def my_func(a):
    return a * 2

print(my_func(2))


class OriginalClass:
    def __call__(self, a):
        return a * 2

class DecoratorClass:
    def __init__(self, wrapee):
        self.wrapee = wrapee

    def __call__(self, a):
        result = self.wrapee(a)
        return result + 3


original_class = OriginalClass()
decorated_class = DecoratorClass(original_class)
print(decorated_class(2))




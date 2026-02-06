def add_n_numbers(*args):
    sum = 0
    for number in args:
        sum += number
    return sum


# print(add_n_numbers(5, 10,  20, 30, 50, 40, 100))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply = 5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]



my_car = Car(model="GT-R", make="Nissan")
print(my_car.make)
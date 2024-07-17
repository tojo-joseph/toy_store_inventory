import functools

# list of of toy prices and quantities
toy_inventory = [
    (140, 5),
    (200, 20),
    (300, 0),
    (500, 6),
    (250, 0),
    (390, 37),
    (400, 45),
    (720, 0),
    (800, 20),
    (900, 17),
    (725, 0),
    (560, 27),
    (890, 33),
    (890, 0),
]

# calculate the total value of each type of toy
def calculate_value(x):
    return x[0] * x[1]

def calculate_toy_value(toy_list):
    return list(map(calculate_value, toy_list))

def total_stock_cost(final_list):
    toys_in_stock = list(filter(lambda x: x[1] > 0, final_list))
    stock_toys_value = list(map(calculate_value, toys_in_stock))
    print(f"Stock TOys Value: {stock_toys_value}")
    return functools.reduce(add, stock_toys_value)

def add(sum_so_far, y):
    return sum_so_far + y

calculate_toy_value(toy_inventory)
total_stock_cost(toy_inventory)
print(f"Value: {calculate_toy_value(toy_inventory)}")
print(f"Total Cost of Toys in Stock: {total_stock_cost(toy_inventory)}")

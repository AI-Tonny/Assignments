# 1
def odds_numbers(left: int, right: int):
    for i in range(left, right + 1, 2):
        yield i

for odd_number in odds_numbers(1, 11):
    print(odd_number, end=" ")

print()

# 2
def numbers_out_of_range(numbers: list[int], left: int, right: int):
    for number in numbers:
        if not left < number < right:
            yield number

list_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number_out_of_range in numbers_out_of_range(list_numbers, 4, 8):
    print(number_out_of_range, end=" ")

print()

# 3
def show_line(symbol: str, function_to_call):
    function_to_call(symbol)

def draw_horizontal_line(symbol: str):
    print(f"{symbol} " * 10)

def draw_vertical_line(symbol: str):
    print(f"{symbol}\n" * 10)

show_line("*", draw_horizontal_line)
show_line("*", draw_vertical_line)

# 4
import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {(end_time - start_time):.4f} seconds...")

        return result
    return wrapper

@execution_time
def evens_numbers_between_0_100000():
    return [number for number in range(0, 100000, 2)]

print(evens_numbers_between_0_100000()[:50])

# 5
@execution_time
def evens_numbers_between_left_right(left: int, right: int):
    return [number for number in range(left, right, 2)]

print(evens_numbers_between_left_right(5000, 10000)[:50])
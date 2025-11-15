numbers_first = (4, 1, 9, 2, 5, 8)
numbers_second = (4, 3, 2, 9, 8, 10)
numbers_third = (4, 1, 7, 9, 3, 2)

numbers_in_all_three = set(numbers_first) & set(numbers_second) & set(numbers_third)
print(numbers_in_all_three)

unique_numbers_first = set(numbers_first) - (set(numbers_second) | set(numbers_third))
unique_numbers_second = set(numbers_second) - (set(numbers_first) | set(numbers_third))
unique_numbers_third = set(numbers_third) - (set(numbers_second) | set(numbers_first))
print(unique_numbers_first)
print(unique_numbers_second)
print(unique_numbers_third)

numbers_in_same_position = [number_first for number_first, number_second, number_third in zip(numbers_first, numbers_second, numbers_third) if number_first == number_second == number_third]
print(numbers_in_same_position)

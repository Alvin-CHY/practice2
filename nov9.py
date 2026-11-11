import copy

fruits = ['apple', 'banana', ['orange', 'grape']]
shallow_fruits = copy.copy(fruits)
deep_fruits = copy.deepcopy(fruits)

shallow_fruits[2][0] = 'kiwi'
deep_fruits[2][1] = 'mango'

print("Original fruits:     ", fruits)
print("Shallow copy fruits: ", shallow_fruits)
print("Deep copy fruits: ", deep_fruits)



numbers = [10, 20, 30, 40, 50, 60, 70, 80]

deep_number = copy.deepcopy(numbers)
deep_number.insert(3, 99)
reversed_number = deep_number[::-1]
sliced_numbers = reversed_number[1:6:2]
print(sliced_numbers)

print(deep_number)
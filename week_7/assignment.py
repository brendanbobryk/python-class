print("\nExcercise 1:\n---------------")
sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500

print(sample_dict)

print("\nExcercise 2:\n---------------")

book_set = {'Harry Potter', 'Angels and Demons'}

book_set.update(['Atlas Shrugged', 'Ulysses'])

print(book_set)
# Question 1:
# Write a Python class to get all possible unique subsets from a set of distinct integers.
# Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class Subsets:
    def get_subsets(self, numbers):
        result = [[]]

        for number in numbers:
            new_subsets = []

            for subset in result:
                new_subsets.append(subset + [number])

            result.extend(new_subsets)

        return result
    
# Test input
numbers = [4, 5, 6]

subset_finder = Subsets()
subsets = subset_finder.get_subsets(numbers)

# Display results
print("Input:", numbers)
print("Output:", subsets)
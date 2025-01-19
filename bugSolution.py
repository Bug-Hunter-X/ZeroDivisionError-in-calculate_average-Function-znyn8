def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

#Improved version to handle potential exceptions more gracefully
def calculate_average_improved(numbers):
    try:
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 0  # Handle cases with non-numeric data

my_list = [1, 2, 3, 4, 5]
result = calculate_average_improved(my_list)
print(f"The improved average is: {result}")

my_list = []
result = calculate_average_improved(my_list)
print(f"The improved average is: {result}")

my_list = [1,2,'a']
result = calculate_average_improved(my_list)
print(f"The improved average is: {result}") 
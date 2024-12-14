from statistics import mean ,median ,mode
numbers = [int(x) for x in input("Enter multiple integers separated by spaces: ").split()]

mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
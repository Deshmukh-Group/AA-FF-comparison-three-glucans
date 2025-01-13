def calculate_percentage_in_range(filename, lower_bound, upper_bound):
    # Read the data from the file
    with open(filename, 'r') as file:
        data = file.readlines()
    
    # Convert the data to float and filter within the range
    values = [float(line.strip()) for line in data]
    in_range_values = [value for value in values if lower_bound <= value <= upper_bound]
    
    # Calculate the percentage
    total_values = len(values)
    in_range_count = len(in_range_values)
    percentage_in_range = (in_range_count / total_values) * 100
    
    # Print the result
    print(f"Percentage of data within range {lower_bound} to {upper_bound}: {percentage_in_range:.2f}%")

# Define the file name and range
filename = 'angle.txt'  # replace with your actual file name
lower_bound = 0.000
upper_bound = 120.000

# Call the function
calculate_percentage_in_range(filename, lower_bound, upper_bound)

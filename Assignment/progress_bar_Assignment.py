'''
Assignment to print the representation
'''



data_set = range(1, 110, 10)
data_set_length = len(data_set)
print("dataset length: ", data_set_length)

for loop_index, _ in enumerate(data_set):
    percent_completed = round((loop_index / (data_set_length - 1)) * 100)
    #print(percent_completed)

    # Calculate the number of asterisks to represent progress
    num_asterisks = int(percent_completed / 10)

    # Print the progress bar with the percentage
    progress_bar = f"[{'*' * num_asterisks}{' ' * (10 - num_asterisks)}] {percent_completed}"
    print(f"{progress_bar}", end="\n")



from time import time
def get_execution_time(func_name):
    """Decorator to calculate and print the execution time of a function"""
    def wrapper(*args, **kwargs):
        print("Inside a decorator")

        #Record the start time
        start = time

        #Execute the decorated function
        result = func_name(*args, **kwargs)

        #Record the end time
        end = time ()

        #Calculate and print the execution time
        execution_time = end-start
        print(f"Execution_time: {execution_time:.6f} seconds")
        return result
    return wrapper

@get_execution_time
def num_generation(start:int, end:int, step:int=1):
    """Function to generate numbers from start to end with a step."""
    nums = []
    for num in range(start, end, step):
        nums.append(nums)
    return nums
# Test case
nums = num_generation(1, 1000000, 2)
print(f"Generated {len(nums)} numbers.") 
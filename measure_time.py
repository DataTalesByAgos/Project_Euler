import time

def measure_time(func, *args):
    """Measures the execution time of a function in milliseconds."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    return result, execution_time
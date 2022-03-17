
# Three ways of doing that:
# + tracking time elaplsed
# + using timeit module  (the most efficient way)
# + special %%timeit "magic-function" for Jupiter Notebook


def func_one(n):
    return [str(num) for num in range(n)]

func_one(10)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def func_two(q):
    return list(map(str,range(q)))

func_two(10)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



# = - = - = - = - = - = - = - = - = - = - = - = - = - =
# TIME ELAPSED:
# = - = - = - = - = - = - = - = - = - = - = - = - = - =
import time


# CURRENT TIME BEFORE CODE EXECUTION
start_time = time.time()

# RUN CODE
result = func_one(1000000)

# CURRENT TIME AFTER CODE EXECUTION
end_time = time.time()

# Elapsed Time
elapsed_time = end_time - start_time

print(elapsed_time)
# 0.3162679672241211


# = - = - = - = - = - = - = - = - = - = - = - = - = - =
# CURRENT TIME BEFORE CODE EXECUTION
start_time2 = time.time()

# RUN CODE
result2 = func_two(1000000)

# CURRENT TIME AFTER CODE EXECUTION
end_time2 = time.time()

# Elapsed Time
elapsed_time2 = end_time2 - start_time2

print(elapsed_time2)
# 0.28658580780029297


# May by unsuitable to measure fast code, showing 0.0 time


# = - = - = - = - = - = - = - = - = - = - = - = - = - =
# TIMEIT:   (Python build in module)
# = - = - = - = - = - = - = - = - = - = - = - = - = - =
import timeit


stmt = '''
func_one(100)
'''

setup = '''
def func_one(u):
    return [str(num) for num in range(u)]
'''


timeit.timeit(stmt,setup,number = 100000)
# 2.649441552999633


# = - = - = - = - = - = - = - = - = - = - = - = - = - =
# Ex 2:

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(u):
    return [str(num) for num in range(u)]
'''


timeit.timeit(stmt2,setup2,number = 100000)



# = - = - = - = - = - = - = - = - = - = - = - = - = - =
# %%timeit (Magic method) for Jupiter Notebook:
# = - = - = - = - = - = - = - = - = - = - = - = - = - =
'''
%%timeit
func_one(100)

# No need to provide Setup.
# 30 µs ± 3.23 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)



%%timeit
func_two(100)

# No need to provide Setup.
# 23.1 µs ± 734 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
'''

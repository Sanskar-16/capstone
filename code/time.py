import timeit

code = """[4, 2, 3, 1, 5].sort()"""

execution_time = timeit.timeit(code, number=1)

print(execution_time)

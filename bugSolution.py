def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Handle division by zero with Infinity
    else:
        return a + b

result = function_with_uncommon_error(0, 5)
print(result)

#Alternative solution: raise exception for better error handling
def function_with_uncommon_error(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero error")
    else:
        return a + b

try:
    result = function_with_uncommon_error(0,5)
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)
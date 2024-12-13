def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a # ZeroDivisionError, but with nuanced handling
    else:
        return a + b

result = function_with_uncommon_error(0, 5)
print(result)
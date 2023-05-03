
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }

    is_float = kwargs.get('make_float', False)

    operation_value = operation_lookup[kwargs.get('operation', '')]

    if is_float:
        final = f"{kwargs.get('message','The result is')} {float(operation_value)}"
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

print(calculate(operation = "multiply", make_float = True, first = 56, second = 56))
# 'The result is 3136.0'

# python dict_unpacking_test.py
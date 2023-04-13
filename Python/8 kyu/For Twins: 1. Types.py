def type_validation(variable, _type):
    if type(variable) == int:
        _t = "int"
    elif type(variable) == str:
        _t = "str"

    return _t == _type

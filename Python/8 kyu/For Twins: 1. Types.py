def type_validation(variable, _type):
    if type(variable) == int:
        return "int" == _type
    elif type(variable) == str:
        return "str" == _type

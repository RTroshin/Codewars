def logical_calc(arr, op):
    match op:
        case 'AND':
            for i in arr[1:]:
                arr[0] &= i
            return arr[0]
        case 'OR':
            for i in arr[1:]:
                arr[0] |= i
            return arr[0]
        case 'XOR':
            for i in arr[1:]:
                arr[0] ^= i
            return arr[0]

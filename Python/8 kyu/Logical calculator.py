def logical_calc(arr, op):
    match op:
        case 'AND':
            for i in range(1, len(arr)):
                arr[0] &= arr[i]
            return arr[0]
        case 'OR':
            for i in range(1, len(arr)):
                arr[0] |= arr[i]
            return arr[0]
        case 'XOR':
            for i in range(1, len(arr)):
                arr[0] ^= arr[i]
            return arr[0]

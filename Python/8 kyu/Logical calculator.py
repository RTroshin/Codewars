def logical_calc(arr, op):
    sum = arr[0]

    match op:
        case 'AND':
            for i in range(1, len(arr)):
                sum &= arr[i]
            return sum
        case 'OR':
            for i in range(1, len(arr)):
                sum |= arr[i]
            return sum
        case 'XOR':
            for i in range(1, len(arr)):
                sum ^= arr[i]
            return sum

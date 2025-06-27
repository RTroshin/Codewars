def divisors(integer):

    for i in range(2, integer):
        if not integer % i:
            break
    else:
        return f"{integer} is prime"

    return [i for i in range(2, integer) if not integer % i]

def tail_swap(lst):
    return [':'.join([lst[0].split(':')[0], lst[1].split(':')[1]])] +\
           [':'.join([lst[1].split(':')[0], lst[0].split(':')[1]])]

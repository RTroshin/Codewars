def tail_swap(strings):
    return [':'.join([strings[0].split(':')[0], strings[1].split(':')[1]])] + [':'.join([strings[1].split(':')[0], strings[0].split(':')[1]])]

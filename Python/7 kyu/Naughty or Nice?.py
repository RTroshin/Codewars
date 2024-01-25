def what_list_am_i_on(actions):
    return "nice" if sum(1 for str in actions if str[0] in "gsn") > sum(1 for str in actions if str[0] in "bfg") else "naughty"

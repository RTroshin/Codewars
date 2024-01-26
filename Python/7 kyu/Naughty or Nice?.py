def what_list_am_i_on(acts):
    return "nice" if sum(1 for str in acts if str[0] in "gsn") > sum(1 for str in acts if str[0] in "bfg") else "naughty"

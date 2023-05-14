def well(x):
    if not 'good' in x:
        return 'Fail!'
    elif x.count('good') > 1:
        return 'I smell a series!'
    else:
        return 'Publish!'

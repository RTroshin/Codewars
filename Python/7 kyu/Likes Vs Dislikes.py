from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    res_state = Nothing

    if lst:
        for state in lst:
            res_state = Nothing if res_state == state else state
    
    return res_state

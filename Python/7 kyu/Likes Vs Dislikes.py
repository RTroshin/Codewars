from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    state = Nothing

    for but in lst:
        state = Nothing if state == but else but
    
    return state

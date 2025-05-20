def solution(full_text, search_text):
    full_text = full_text.split(search_text)
    
    return len(full_text) - 1

def baby_shark_lyrics():
    s = " shark"
    doo = " doo" * 6
    sharks = [f"Baby{s}", f"Mommy{s}", f"Daddy{s}", f"Grandma{s}", f"Grandpa{s}", "Let's go hunt"]
    res = ''

    for i in range(len(sharks)):
        res += f"{sharks[i]},{doo}\n" * 3 + f"{sharks[i]}!\n"

    return f"{res}Run away,…"

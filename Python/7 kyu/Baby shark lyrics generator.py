def baby_shark_lyrics():
    s = " shark"
    sharks = [f"Baby{s}", f"Mommy{s}", f"Daddy{s}", f"Grandma{s}", f"Grandpa{s}", "Let's go hunt"]

    return ''.join(f"{sharks[i]},{' doo' * 6}\n" * 3 + f"{sharks[i]}!\n" for i in range(6)) + "Run away,…"

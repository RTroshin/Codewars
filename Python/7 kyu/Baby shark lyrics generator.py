def baby_shark_lyrics():
    s = " shark"
    doo = " doo" * 6
    sharks = ["Baby", "Mommy", "Daddy", "Grandma", "Grandpa", "Let's go hunt"]
    res = ''

    for i in range(len(sharks) - 1):
        res += f"{sharks[i]}{s},{doo}\n" * 3 + f"{sharks[i]}{s}!\n"

    res += f"Let's go hunt,{doo}\n" * 3 + f"Let's go hunt!\n"
    return res + "Run away,…"

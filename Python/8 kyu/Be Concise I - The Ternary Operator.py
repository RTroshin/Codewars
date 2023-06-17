def describe_age(n):
    return "You're a(n) " + ("kid" if n < 13 else "teenager" if n < 18 else "adult" if n < 65 else "elderly")

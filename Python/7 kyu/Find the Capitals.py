def capital(capitals):
    return [f"The capital of {c.get('state') or c.get('country')} is {c.get('capital')}" for c in capitals]

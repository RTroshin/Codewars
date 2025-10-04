def capital(capitals):
    res = []

    for i in range(len(capitals)):
        res.append("The capital of " + capitals[i].get("state") + " is " + capitals[i].get("capital"))

    return res

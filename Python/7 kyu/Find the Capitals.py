def capital(capitals):
    res = []

    for i in range(len(capitals)):
        res.append("The capital of " + (capitals[i].get("state") or capitals[i].get("country")) + " is " + capitals[i].get("capital"))

    return res

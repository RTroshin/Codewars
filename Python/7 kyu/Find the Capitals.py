def capital(capitals):
    return ["The capital of " + (capitals[i].get("state") or capitals[i].get("country")) + " is " + capitals[i].get("capital") for i in range(len(capitals))]

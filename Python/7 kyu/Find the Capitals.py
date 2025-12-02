def capital(capitals):
    return ["The capital of " + (cap.get("state") or cap.get("country")) + " is " + cap.get("capital") for cap in capitals]

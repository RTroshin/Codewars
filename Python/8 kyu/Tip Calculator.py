def calculate_tip(amount, rating):
    match rating.lower():
        case "terrible":
            return 0
        case "poor":
            return -1 * amount * 5 // 100 * -1
        case "good":
            return -1 * amount * 10 // 100 * -1
        case "great":
            return -1 * amount * 15 // 100 * -1
        case "excellent":
            return -1 * amount * 20 // 100 * -1
    return "Rating not recognised"

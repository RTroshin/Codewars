def calculate_tip(amount, rating):
    match rating.lower():
        case 'terrible':
            return amount
        case 'poor':
            return int(-1 * amount * 5 // 100 * -1)
        case 'good':
            return int(-1 * amount * 10 // 100 * -1)
        case 'great':
            return int(-1 * amount * 15 // 100 * -1)
        case 'excellent':
            return int(-1 * amount * 20 // 100 * -1)
    return 'Rating not recognised'

turkish_numbers = {0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş",
                   6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz", 10: "on",
                   20: "yirmi", 30: "otuz", 40: "kırk", 50: "elli",
                   60: "altmış", 70: "yetmiş", 80: "seksen", 90: "doksan"}

def get_turkish_number(num):
    if num < 10:
        return turkish_numbers.get(num)
    elif num >= 10 and num < 20:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 10)
    elif num >= 20 and num < 30:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 20)
    elif num >= 30 and num < 40:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 30)
    elif num >= 40 and num < 50:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 40)
    elif num >= 50 and num < 60:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 50)
    elif num >= 60 and num < 70:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 60)
    elif num >= 70 and num < 80:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 70)
    elif num >= 80 and num < 90:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 80)
    elif num >= 90 and num < 100:
        return turkish_numbers.get(num // 10 * 10) + ' ' + turkish_numbers.get(num - 90)

def HQ9(code):
    match code:
        case 'H':
            return "Hello World!"
        case 'Q':
            return code
        case '9':
            BottlesOfBeer = ""

            for i in range(100, 1, -1):
                if i > 3:
                    BottlesOfBeer += str(i - 1) + \
                    " bottles of beer on the wall, " + \
                    str(i - 1) + \
                    " bottles of beer.\n" + \
                    "Take one down and pass it around, " + \
                    str(i - 2) + \
                    " bottles of beer on the wall.\n"
                elif i > 2:
                    BottlesOfBeer += str(i - 1) + \
                    " bottles of beer on the wall, " + \
                    str(i - 1) + \
                    " bottles of beer.\n" + \
                    "Take one down and pass it around, " + \
                    str(i - 2) + \
                    " bottle of beer on the wall.\n"
                else:
                    BottlesOfBeer += str(i - 1) + \
                    " bottle of beer on the wall, " + \
                    str(i - 1) + \
                    " bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n"

            return BottlesOfBeer + "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        case 'X':
            return None

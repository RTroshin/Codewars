def i_speak_french(sentence):
    return ' '.join(["Baguette"] + ["baguette"] * len(sentence.split()) - 1 + ["Encore!"])

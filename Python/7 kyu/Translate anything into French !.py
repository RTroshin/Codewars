def i_speak_french(sentence):
    lenSentence = len(sentence.split()) - 1

    return ' '.join(["Baguette"] + ["baguette"] * lenSentence + ["Encore!"])

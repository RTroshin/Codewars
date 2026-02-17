def i_speak_french(sentence):
    sentence = sentence.split()
    lenSentence = len(sentence) - 1

    return ' '.join(["Baguette"] + ["baguette"] * lenSentence + ["Encore!"])

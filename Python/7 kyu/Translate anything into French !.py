def i_speak_french(sentence):
    res = []
    sentence = sentence.split()
    lenSentence = len(sentence) - 1

    res = ["Baguette"] + ["baguette"] * lenSentence + ["Encore!"]
    res = ' '.join(res)

    return res

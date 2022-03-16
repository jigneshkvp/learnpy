def sentence_maker(txt: str) -> str:
    question_words = ("how", "where", "when", "what", "which", "why")
    cap_txt = txt.capitalize()
    if txt.startswith(question_words):
        return "{}?".format(cap_txt)
    else:
        return "{}.".format(cap_txt)


results = []
while True:
    in_text = input("Say something: ")
    if in_text == "\end":
        break
    else:
        results.append(sentence_maker(in_text))

print(" ".join(results))

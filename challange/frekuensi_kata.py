import string

def word_freq(text: str):
    punct = ".,!?;:"
    trans = str.maketrans("", "", punct)
    cleaned = text.lower().translate(trans)
    words = cleaned.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return items

text = "Python itu mudah, dan python itu kuat!"
for w, c in word_freq(text):
    print(w, c)

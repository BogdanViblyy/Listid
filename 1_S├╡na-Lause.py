# Sisestage sõna või lause klaviatuurilt ja loendage, mitu vokaali ja mitu konsonanti selles on.
# Kui on sisestatud lause, loendage ka kirjavahemärgid ja tühikud.


userInput = input("Sisestage sõna või lause: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',  'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
punctuation = ['.', ',', ';', ':', '!', '?', '-', '—', '(', ')', '[', ']', '{', '}', '"', '\'', '«', '»', '…']

vowelsCount = 0
consonantsCount = 0
punctuationCount = 0
spacesCount = 0

for item in userInput.lower():
    if item in vowels:
        vowelsCount += 1
    elif item in consonants:
        consonantsCount += 1
    elif item in punctuation:
        punctuationCount += 1
    elif item == ' ':
        spacesCount += 1

print(f'Täishäälikud: {vowelsCount}, Kaashäälikud: {consonantsCount}, Kirjavahemärgid: {punctuationCount}, Tühikud: {spacesCount}')

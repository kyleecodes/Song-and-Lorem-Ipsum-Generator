from random import choice
import sys
from get_lyrics import scrape_song_lyrics, request_song_url, get_lyrics


def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i:i + order]
        next_letter = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if next_letter not in model[fragment]:
            model[fragment][next_letter] = 1
        else:
            model[fragment][next_letter] += 1
    return model


def getNextCharacter(model, fragment):
    letters = []
    for letter in model[fragment].keys():
        for times in range(0, model[fragment][letter]):
            letters.append(letter)
    return choice(letters)


def generate_text(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0:order]
    output = ""
    for i in range(0, length - order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1:] + newCharacter
    print(output)


# lyrics = get_lyrics('Ariana Grande', 100)

if __name__ == "__main__":
    artist = input("Enter the musical artist you'd like to use for reference: \n")
    lyrics = get_lyrics(f'{artist}', 100)
    generate_text(lyrics, 3, 10000)

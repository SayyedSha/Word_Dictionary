import requests
import random

# A small list of words you can expand later or use a word API
words = [
    "serendipity", "ephemeral", "luminous", "eloquent",
    "labyrinth", "quintessential", "zealous", "mellifluous",
    "ambiguous", "sonder"
]

def get_word_of_the_day():
    word = random.choice(words)
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[0]
        word = data['word']
        meanings = data['meanings'][0]
        part_of_speech = meanings['partOfSpeech']
        definition = meanings['definitions'][0]['definition']
        example = meanings['definitions'][0].get('example', "No example available.")

        print(f"\n📘 Word of the Day: {word.capitalize()}")
        print(f"🔤 Part of Speech: {part_of_speech}")
        print(f"📖 Definition: {definition}")
        print(f"💬 Example: {example}\n")
    else:
        print("❌ Failed to fetch definition. Try again later.")

get_word_of_the_day()

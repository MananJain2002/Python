import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}

word = input("Enter a word: ").upper()
print([phonetic_dict[w] for w in word])
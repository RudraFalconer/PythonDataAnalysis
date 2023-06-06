import csv
from functions import remove_special_characters
from stopwords import stopwords
from functions import remove_stopwords
import functions
dataset = []

with open('twitter_reduced.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        dataset.append(row)

# Mostrar los 5 primeros registros
for i in range(5):
    print(dataset[i])


dataset = remove_special_characters(dataset)
for i in range(5):
    print(dataset[i])

dataset = remove_stopwords(dataset)
last_five_entries = dataset[-5:]
for entry in last_five_entries:
    print(entry)
    
word_frequencies, unique_words = functions.bag_of_words(dataset)
first_10_word_frequencies = dict(list(word_frequencies.items())[:10])

print(first_10_word_frequencies)